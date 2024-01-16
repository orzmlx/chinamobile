from collections import deque
import pandas as pd
import logging
import os
import re
import huaweiconfiguration
import huaweiutils


class HuaweiRawDataFile(object):
    def __init__(self, raw_data_inpath, command_file_path, out_path, common_table, need_params):
        self.to_be_continue = False
        self.demand_params, self.merge_params = self.parse_param(need_params)
        self.out_put_dict = {}
        self.common_table = common_table
        self.checked_unit_number = 0
        self.command_col_dict = {}
        self.__word__method = {"成功条数": "get_success_number",
                               "失败条数": "get_fail_number",
                               huaweiconfiguration.COMMAND: "get_command",
                               "网元": "get_network_element",
                               "报文": "get_message",
                               huaweiconfiguration.RETURN_CODE: "get_return_code",
                               huaweiconfiguration.QUERY: "get_command_meaning"}
        self.__current_phase = "成功条数"
        self.fail_phases = deque(["失败条数", huaweiconfiguration.COMMAND, "网元", "报文"])
        self.success_phases = deque(
            [huaweiconfiguration.COMMAND, "网元", "报文", huaweiconfiguration.RETURN_CODE, huaweiconfiguration.QUERY])
        self.phases_dict = {huaweiconfiguration.COMMAND: [], "网元": [], "报文": [],
                            huaweiconfiguration.RETURN_CODE: [], huaweiconfiguration.QUERY: []}
        self.raw_data_inpath = raw_data_inpath
        self.out_path = out_path
        self.fail_command_number = 0
        self.success_command_number = 0
        self.command_content_dict = {}
        self.content_dict = {}
        self.command_path = command_file_path
        self.command_list = self.read_command_list()
        assert len(self.command_list) == len(huaweiconfiguration.COMMAND_LIST), "配置和输入命令长度不相等"
        self.init_table()
        self.current_command = ""
        self.exist_cols = []
        self.current_network_element = ""
        self.files_cols_dict = {}

    def parse_param(self, params):
        result = []
        merge_params = {}
        for p in params:
            p = p.strip().replace(" ", "")
            if p.find("&") >= 0 and p.find(":") >= 0:
                splits = p.split(":")
                col_name = splits[0]
                params = splits[1].split("&")
                result.extend(params)
                merge_params[col_name] = params
            else:
                result.append(p)
        return result, merge_params

    @staticmethod
    def init_dict(new_list, new_dict):
        for e in new_list:
            e = e.strip()
            if e not in new_dict:
                new_dict[e] = []

    def init_table(self):
        """
            初始化基本信息
        """
        for i in range(len(huaweiconfiguration.COMMAND_LIST)):
            new_dict = {}
            e = huaweiconfiguration.COMMAND_LIST[i]
            # 去掉列名中的空格
            e = [s.replace(' ', '') for s in e]
            self.init_dict(e, new_dict)
            key = huaweiconfiguration.COMMAND_NAME_LIST[i]
            self.command_content_dict[key] = new_dict
            self.command_col_dict[key] = e

    def read_huawei_txt(self):
        return_code = -1
        phases = self.fail_phases
        with open(self.raw_data_inpath, 'r') as f:
            line = f.readline()
            while line:
                print(line)
                if line.find(self.__current_phase) == 0:
                    if self.__current_phase == "报文" and return_code == -1:
                        self.phases_dict[huaweiconfiguration.RETURN_CODE].append(return_code)
                        self.phases_dict[huaweiconfiguration.QUERY].append(huaweiconfiguration.EMPTY_VALUE)
                    method_name = self.__word__method[self.__current_phase]
                    func = getattr(self, method_name)
                    if not callable(func):
                        logging.error(method_name + "不可用")
                        return
                    func(line)
                    ##如果是查询命令阶段,那么继续解读命令
                    if self.__current_phase == huaweiconfiguration.QUERY:
                        line = f.readline()
                        if len(line) > 0 and line.find("-") == 0:
                            line = f.readline()
                            self.parse_message_content(line, f)
                    self.__current_phase = phases.popleft()
                    if self.__current_phase != "成功条数" and self.__current_phase != "失败条数":
                        phases.append(self.__current_phase)
                line = f.readline()
                if self.to_be_continue is True:
                    self.__current_phase = huaweiconfiguration.RETURN_CODE
                    phases = deque([huaweiconfiguration.QUERY, huaweiconfiguration.COMMAND,
                                    "网元", "报文", huaweiconfiguration.RETURN_CODE])
                    self.to_be_continue = False
                if line.find("没有查到相应的结果") >= 0:
                    self.phases_dict[huaweiconfiguration.QUERY].append("没有查到相应的结果")
                    self.__current_phase = phases.popleft()
                    phases.append(self.__current_phase)
                if line.find("成功命令") >= 0:
                    phases = self.success_phases
                    self.__current_phase = phases.popleft()
                    phases.append(self.__current_phase)
                    return_code = 0

    def get_message(self, line):
        self.phases_dict["报文"].append(line.split(":")[1].replace("\n", ""))

    def get_command_meaning(self, line):
        self.phases_dict[huaweiconfiguration.QUERY].append(line.split(huaweiconfiguration.QUERY)[1].replace("\n", ""))

    def get_return_code(self, line):
        pattern = r'\d+'
        self.phases_dict[huaweiconfiguration.RETURN_CODE].append(re.findall(pattern, line)[0])

    def read_command_list(self):
        command_list = []
        with open(self.command_path, 'r') as f:
            line = f.readline()
            while line:
                line = line.replace("\n", "")
                command_list.append(line)
                line = f.readline()
        return list(filter(lambda x: x.strip() != "", command_list))

    def get_command(self, line):
        command = line.split("-----")[1].replace("\n", "")
        self.phases_dict["命令"].append(command)
        self.current_command = command

    def get_network_element(self, line):
        current_network_element = line.split(":")[1].replace("\n", "")
        self.phases_dict["网元"].append(line.split(":")[1].replace("\n", ""))
        self.current_network_element = current_network_element

    def parse_message_content(self, line, f):
        """
            此时的Line是第一行数据
            如果结果中含有等号,那么查询结果只有一行
        """
        if line.find("=") >= 0:
            unit_number = self.__read_one_unit_message(f, line)
        # 说明结果是多行
        else:
            unit_number = self.__read_multi_unit_message(f, line)
        if unit_number > 0:
            self.__check_exist_cols(unit_number)

    def __check_exist_cols(self, add_number):
        expect_cols = self.command_col_dict[self.current_command]
        if len(expect_cols) != len(self.exist_cols):
            # 缺少的列
            different_cols = set(expect_cols).difference(set(self.exist_cols))
            both_different_cols = set(expect_cols) ^ set(self.exist_cols)
            if len(different_cols) != len(both_different_cols):
                logging.info("列名待补充")
            if len(different_cols) > 0:
                command_dict = self.command_content_dict[self.current_command]
                for col in different_cols:
                    for i in range(add_number):
                        self.__init_content_dict(col, huaweiconfiguration.EMPTY_VALUE, command_dict)
        self.exist_cols = []

    def get_success_number(self, line):
        self.success_command_number = int(line.split(":")[1].replace("\n", ""))

    def get_fail_number(self, line):
        self.fail_command_number = int(line.split(":")[1].replace("\n", ""))

    def __read_one_unit_message(self, f, line):
        """
            在华为原始文件中读取单行结果
        """
        command_dict = self.command_content_dict[self.current_command]
        latest_col = ""
        latest_value = ""
        self.exist_cols.append("网元")
        self.__init_content_dict("网元", self.current_network_element, command_dict)
        while line:
            line = line.replace("\n", "")
            if len(line) == 0:
                line = f.readline()
                continue
            if line.find(huaweiconfiguration.END) >= 0:
                self.__init_content_dict(latest_col, latest_value, command_dict)
                return 1
            if line.find("结果个数") >= 0:
                line = f.readline()
                continue
            if line.find("共有") >= 0:
                line = f.readline()
                continue
            if line.find("仍有后续报告输出") >= 0:
                self.to_be_continue = True
                line = f.readline()
                continue
            splits = line.split("=")
            col_name = splits[0].strip().replace(" ", "")
            value = splits[1].strip()
            # 如果col列有值,value也有值
            if len(col_name) > 0 and len(value) > 0:
                if col_name != latest_col:
                    """
                        如果当前的colname不等于上一行的colname,并且上一行的colname和值都不为空，说明这是新的一列，将上一列
                        的col和value存起来
                     """
                    if latest_col != "" and latest_value != "":
                        self.__init_content_dict(latest_col, latest_value, command_dict)
                    latest_col = col_name
                    latest_value = value
                self.exist_cols.append(col_name)
            elif len(col_name) == 0 and len(value) > 0:
                latest_value = latest_value + "&" + value
            else:
                logging.error(line + ":无法解析")
            line = f.readline()
        return 1

    @staticmethod
    def __init_content_dict(key, value, new_dict):
        key = key.strip().replace(" ", "")
        value = value.strip()
        if key in new_dict:
            new_dict[key].append(value.strip())
        else:
            new_dict[key] = []
            if len(value) > 0:
                new_dict[key].append(value)

    def __merge_same_command_data(self):
        """
            将相同命令但是后面参数不同的数据合并在一起
            例如LST NRCELLQCIBEARER:QCI=1和LST NRCELLQCIBEARER:QCI=2命令
            下的数据合并在一起
        """
        out_put_dict = {}
        for d in self.command_content_dict:
            logging.info(d)
            file_name = d.replace(":", "").replace(";", "")
            df = pd.DataFrame(self.command_content_dict[d])
            # NRDU小区改成NR小区
            if ~df.empty:
                df.reset_index(inplace=True, drop=True)
                cols = df.columns.tolist()
                if "NRDU小区标识" in cols:
                    df.rename(columns={"NRDU小区标识": "NR小区标识"}, inplace=True)
                out_name = file_name + ".csv"
                if len(out_put_dict) == 0:
                    out_put_dict[out_name] = df
                    continue
                is_add = False
                for f, pre_df in out_put_dict.items():
                    res = ''.join(set(out_name) ^ set(f))
                    if len(res) == 0:
                        continue
                    if res.isdigit() is True and len(out_name) == len(f):
                        pre_df = pd.concat([pre_df, df], axis=0)
                        out_put_dict[f] = pre_df
                        is_add = True
                        break
                if is_add is False:
                    out_put_dict[out_name] = df
        self.out_put_dict = out_put_dict

    # 合并所需要的数据
    def find_params(self, out_put_dict, key_col, exclude):
        res = pd.DataFrame()
        for f, df in out_put_dict.items():
            if len(exclude) > 0 and f in exclude:
                continue
            if len(df) == 0:
                continue
            find = False
            output_cols = ['网元']
            cols = df.columns.tolist()
            first_row = df.iloc[0]
            common_intersection = list(set(cols) & set(self.demand_params))
            key_intersection = list(set(cols) & set(key_col))
            if len(common_intersection) > 0:
                find = True
                output_cols.extend(common_intersection)
            if len(key_intersection) > 0:
                find = True
                output_cols.extend(key_intersection)
            if 'NR小区标识' in cols:
                output_cols.append('NR小区标识')
            main_col_result = df[output_cols]

            for c in cols:
                cell = first_row[c]
                for param in self.demand_params:
                    find_result = str(cell).find(param)
                    if int(find_result) >= 0:
                        find = True
                        flatten_df = huaweiutils.flatten_features(df, c)
                        children_cols = ['网元', param]
                        if 'NR小区标识' in cols:
                            children_cols.append('NR小区标识')
                        flatten_df = flatten_df[children_cols]
                        main_col_result = main_col_result.merge(flatten_df, how='left', on=['网元', 'NR小区标识'])
            if find is True:
                if res.empty:
                    res = main_col_result
                else:
                    res = res.merge(main_col_result, how='left', on=['网元', 'NR小区标识'])
        return res

    def get_base_info(self, out_put_dict):
        """
            获取基本信息列
        """
        ducell_df = out_put_dict['LST NRDUCELL.csv']
        gnode_df = out_put_dict['LST GNODEBFUNCTION.csv']
        ducell_df = huaweiutils.add_cgi(ducell_df, gnode_df)
        common_table = pd.read_csv(self.common_table, usecols=['覆盖类型', '覆盖场景', 'CGI', '地市'], encoding='gbk')
        # 覆盖类型中，室内外和空白，归为室外
        common_table['覆盖类型'] = common_table['覆盖类型'].map({"室外": "室外", "室内外": "室外", "室内": "室内"})
        common_table['覆盖类型'].fillna("室外", inplace=True)
        # huaweiutils.output_csv(common_table, "common.csv", self.out_path)
        ducell_df['CGI'] = "460-00-" + ducell_df["gNodeB标识"].apply(str) + "-" + ducell_df["NR小区标识"].apply(str)
        base_info_df = ducell_df[['网元', 'NR小区标识', 'NRDU小区名称', 'CGI', '频带', '双工模式']]
        # base_info_df = base_info_df.rename(columns={'NRDU小区标识': 'NR小区标识'})
        base_info_df = base_info_df.merge(common_table, how='left', on=['CGI'])
        base_info_df['厂家'] = '华为'
        return base_info_df

    def output_content_dict(self):
        """
            华为按命令行导出数据
        """
        self.__merge_same_command_data()
        for f, df in self.out_put_dict.items():
            huaweiutils.output_csv(df, f, self.out_path)
            self.files_cols_dict[f] = df.columns.tolist()

    def output_handover_result(self, qci):
        """
            根据输入的核查参数名字，输出切换参数并输出结果
        """
        # 过滤出需要的列,并且合成一张表
        base_info_df = self.get_base_info(self.out_put_dict)
        key_col = ['异系统切换至E-UTRAN测量参数组标识', '异频切换测量参数组标识', '异系统切换测量参数组标识']
        result = self.find_params(self.out_put_dict, key_col, ['LST NRCELLQCIBEARERQCI=1.csv'])
        key_col_qci = ['服务质量等级', '异系统切换测量参数组标识', '异系统切换至E-UTRAN测量参数组标识', '异频切换测量参数组标识']
        qci_result = self.find_params(
            {'LST NRCELLQCIBEARERQCI=1.csv': self.out_put_dict['LST NRCELLQCIBEARERQCI=1.csv']},
            key_col_qci, [])
        if qci_result.empty is True:
            raise Exception("QCI数据为空,请检查数据!")
        qci_result = qci_result[qci_result['服务质量等级'] == str(qci)]
        qci_result = qci_result.merge(result, how='left',
                                      on=['网元', 'NR小区标识', '异系统切换测量参数组标识', '异系统切换至E-UTRAN测量参数组标识', '异频切换测量参数组标识'])
        all_result = qci_result.merge(base_info_df, how='left', on=['网元', 'NR小区标识'])
        # 合并参数
        self.join_params(all_result)
        all_result = all_result[huaweiconfiguration.HUAWEI_COLS_ORDER]
        all_result_name = "all_result.csv"
        huaweiutils.output_csv(all_result, all_result_name, self.out_path)

    def __read_multi_unit_message(self, f, line):
        command_dict = self.command_content_dict[self.current_command]
        is_first_line = True
        cols = []
        result_number = 0
        fact_number = 0
        while line:
            line = line.replace("\n", "")
            if len(line) == 0:
                line = f.readline()
                continue
            if line.find(huaweiconfiguration.END) >= 0:
                if int(result_number) != fact_number:
                    logging.warn('实际读取行数和日志行数不一致,请检查数据')
                self.exist_cols = cols
                return fact_number
            if line.find("结果个数") >= 0:
                pattern = r'\d+'
                result_number = re.findall(pattern, line)[0]
                line = f.readline()
                continue
            if line.find("共有") >= 0:
                line = f.readline()
                continue
            if line.find("仍有后续报告输出") >= 0:
                self.to_be_continue = True
                line = f.readline()
                continue
            # 第一行是列名，并且第一列加上网元列
            if is_first_line:
                cols = line.replace("\n", "").split("  ")
                cols = list(filter(lambda x: x.strip() != "", cols))
                # 去掉里面列名中的空格
                cols = [s.replace(' ', '') for s in cols]
                cols.insert(0, '网元')
                is_first_line = False
            else:
                fact_number = fact_number + 1
                row = line.split("  ")
                new_row = [self.current_network_element]
                # 去掉列表中的空格和空列名
                for r in row:
                    r = r.strip()
                    if len(r) == 0:
                        continue
                    new_row.append(r)
                # 每一行都添加网元信息,作为Index,必须是最后一个
                assert len(new_row) == len(cols), "列名长度和内容长度不一致,请检查数据"
                for index, row in enumerate(new_row):
                    col_name = cols[index]
                    value = new_row[index]
                    self.__init_content_dict(col_name, value, command_dict)
            line = f.readline()
        return fact_number

    def join_params(self, all_result):
        for col_name, params in self.merge_params.items():
            if col_name in params:
                all_result[col_name] = all_result[col_name].map({"开": True, "关": False})
                skip_name = col_name
            else:
                all_result[col_name] = all_result[params[0]].map({"开": True, "关": False})
                skip_name = params[0]
            for index, p in enumerate(params):
                if p == skip_name:
                    continue
                all_result[p] = all_result[p].map({"开": True, "关": False})
                all_result[p].fillna(True, inplace=True)
                all_result[col_name] = all_result[col_name] & all_result[p]
                all_result[col_name] = all_result[col_name].map({True: "开", False: "关"})
                all_result.drop(p, axis=1, inplace=True)
        return all_result


if __name__ == "__main__":
    #rawDataPath = "C:\\Users\\No.1\\Downloads\\pytorch\\pytorch\\huawei\\QCI\\华为5G-QCI-159\\MML任务结果_gt_20231226_112108.txt"
    rawDataPath = "C:\\Users\\No.1\\Downloads\\pytorch\\pytorch\\huawei\\MML任务结果_gt_20231225_155211.txt"
    commandPath = "C:\\Users\\No.1\\Downloads\\pytorch\\pytorch\\huawei\\华为45G互操作固定通报参数20231225.txt"
    outputPath = "C:\\Users\\No.1\\Downloads\\pytorch\\pytorch\\huawei\\result"
    # 工参表路径
    common_table = "C:\\Users\\No.1\\Downloads\\pytorch\\pytorch\\huawei\\地市规则\\5G资源大表-20231227.csv"
    rawFile = HuaweiRawDataFile(rawDataPath, commandPath, outputPath, common_table,
                                huaweiconfiguration.HUAWEI_DEMAND_PARAMS)
    rawFile.read_huawei_txt()
    # rawFile.output_handover_result(qci=9)
    rawFile.output_content_dict()
    rawFile.output_handover_result(9)


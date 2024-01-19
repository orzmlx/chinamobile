import pandas as pd
import math
import gutils
from tqdm import tqdm
from shapely.geometry import Point
import copy
import itertools
import common_util


class WeightChange:
    # csv文件解析异常,直接改后缀无法解决，将xlsx另存为包含,的csv文件
    def __init__(self, common_file_path, cloud_file_path, output_path, distance):
        self.output_path = output_path
        self.match_result = {}
        self.cover_distance = distance
        self.common_file_path = common_file_path
        self.cloud_file_path = cloud_file_path
        self.common_file_df = pd.read_csv(self.common_file_path
                                          ,
                                          usecols=["CGI", "地市", "网管中网元名称", "覆盖类型", "覆盖场景", "经度", "纬度", "AAU挂高",
                                                   "总俯仰角", "物理点编号", '是否大于20G', 'CELL区域类别', '方位角']
                                          , encoding='gbk')
        self.cloud_file_df = pd.read_csv(self.cloud_file_path,
                                         usecols=["名称", "地市名称", "经度", "纬度", "MR总数_移动",
                                                  '区域类型'
                                                  # "SSB-RSRP(dBm)_移动",
                                                  # "SSB-DLSINR(dB)_移动",,
                                                  # "下行弱覆盖MR比例(SSB)(%)_移动",
                                                  # "下行质差MR比例(SSB)(%)_移动", "重叠覆盖MR比例(SSB)(%)_移动", "RSRP低于-120的MR数_移动",
                                                  # "RSRP低于-115的MR数_移动",
                                                  # "RSRP低于-110的MR数_移动", "RSRP低于-109的MR数_移动",
                                                  # "RSRP低于-108的MR数_移动", "RSRP低于-107的MR数_移动", "RSRP低于-106的MR数_移动",
                                                  # "RSRP低于-105的MR数_移动", "RSRP低于-104的MR数_移动", "RSRP低于-103的MR数_移动",
                                                  # "RSRP低于-102的MR数_移动", "RSRP低于-101的MR数_移动", "RSRP低于-100的MR数_移动",
                                                  # "RSRP低于-99的MR数_移动", "RSRP低于-98的MR数_移动", "RSRP低于-97的MR数_移动",
                                                  # "RSRP低于-96的MR数_移动", "RSRP低于-95的MR数_移动", "RSRP低于-90的MR数_移动"
                                                  ],
                                         encoding='gbk')
        self.cloud_file_df.rename(columns={"地市名称": "地市"}, inplace=True)
        self.common_file_df.rename(columns={"CELL区域类别": "区域类型"}, inplace=True)
        self.cloud_file_df['地市'] = self.cloud_file_df['地市'].apply(lambda x: x.replace("市(移动定制)", ""))
        self.common_file_df['区域类型'] = self.common_file_df['区域类型'].map({"农村": "四类区域", "三类": "三类区域"})
        self.cloud_file_df['MR总数_移动'].fillna(value=0, inplace=True)

    @staticmethod
    def match_distance_by_geo(lat_node, lon_node, lat, lon, distance):
        """
            根据小数点位数来快速过滤站点
        """
        lat_node_decimal_part = abs(lat_node - lat)
        lon_node_decimal_part = abs(lon_node - lon)
        return False if lat_node_decimal_part > 0.1 \
                        or lon_node_decimal_part > 0.1 else True

    @staticmethod
    def get_match_points(x, cloud_file_df, cover_distance, start_angle, end_angle):
        # 获取每个云勘点的经纬度,与小区经纬度做计算
        lat_node, lon_node = x['纬度'], x['经度']
        city = x['地市']

        match_nodes_names = []
        match_node_list = []
        sum_weight = 0

        # p_node = Point(lon_node, lat_node)
        for lat, lon, c, weight, name in zip(cloud_file_df['纬度'], cloud_file_df['经度'], cloud_file_df['地市'],
                                             cloud_file_df['MR总数_移动'], cloud_file_df['名称']):

            if c != city:
                continue

            match, angle = weightchange.is_in_sector(lat_node, lon_node, lat, lon, start_angle, end_angle,
                                                     cover_distance)
            if match:
                sum_weight = sum_weight + weight
                # cloud_point = Point(lon, lat)
                # is_clock_wise = WeightChange.get_normal_direction(angle, start_angle, end_angle, center_angle, 45)
                # absolute_angle = gutils.get_angle_absolute_value(center_angle, angle)
                # # 云勘点到法线的距离
                # linear_distance = gutils.point_2_vertical_line_distance(cloud_point, p_node, absolute_angle)
                match_node_list.append((weight, lat, lon, name))
                match_nodes_names.append(name)
        return match_node_list, sum_weight, match_nodes_names

    @staticmethod
    def is_in_sector(lat_node, lon_node, lat, lon, start_angle, end_angle, cover_distance):
        if WeightChange.match_distance_by_geo(lat_node, lon_node, lat, lon, cover_distance):
            real_distance = gutils.haversine((lat_node, lon_node), (lat, lon))
            if real_distance < cover_distance:
                angle = gutils.get_angle(lat_node, lon_node, lat, lon)
                if int(angle) < 0:
                    angle = 360 + angle
                if abs(int(end_angle) - int(start_angle)) > 90:
                    return angle <= start_angle or angle >= end_angle, angle
                else:
                    return start_angle <= angle <= end_angle, angle
        return False, None

    # 如果dataFrame中遍历的数据不多，zip()是最高效的遍历方法，速度约是iterrows的300倍
    @staticmethod
    def get_proper_point_by_node(row, cloud_file_df, cover_distance):
        cgi = row['CGI']
        direction = row["方位角"]
        # if direction == 10:
        #     print()
        start_angle, end_angle = gutils.get_rad_by_direction(direction)
        center_angle = weightchange.get_center_angle(end_angle, start_angle, 45)
        height = row['AAU挂高']
        lat_node, lon_node = row['纬度'], row['经度']
        match_node_list, sum_weight, match_node_names = weightchange.get_match_points(row, cloud_file_df,
                                                                                      cover_distance, start_angle,
                                                                                      end_angle)
        pro_lat, pro_lon = weightchange.calculate_proper_point(match_node_list, sum_weight)
        # 获取这个点的方位角
        new_direction = gutils.get_angle(lat_node, lon_node, pro_lat, pro_lon)

        if int(new_direction) < 0:
            new_direction = new_direction + 360
        # 反推方位角
        # new_direction = weightchange.get_new_direction(center_angle, clock_wise_angle, anti_clock_wise_angle)
        # 获取该点到node的距离
        distance = gutils.get_distance(pro_lon, pro_lat, lon_node, lat_node)
        # 反推下倾角
        new_tilt = weightchange.get_new_down_tilt(height, distance)
        # 根据规则调整计算所得下倾角
        adjust_tilt = weightchange.adjust_tilt_by_rule(new_tilt, height)
        # 根据规则调整方位角
        adjust_direction = weightchange.direction_adjust_by_rule(direction, new_direction)
        return start_angle, end_angle, new_direction, adjust_direction, new_tilt, \
               adjust_tilt, sum_weight, pro_lat, pro_lon

    @staticmethod
    def direction_adjust_by_rule(direction, new_direction):
        if abs(new_direction - direction) < 30 or abs(new_direction - direction) > 330:
            return new_direction
        if 330 >= int(new_direction) - int(direction) > 180:
            new_direction = direction - 30
        elif int(new_direction) - int(direction) < -180:
            new_direction = direction + 30
        elif 0 < int(new_direction) - int(direction) <= 180:
            new_direction = direction + 30
        elif -180 <= int(new_direction) <= 0:
            new_direction = direction - 30
        if int(new_direction) > 360:
            new_direction = new_direction - 360
        elif int(new_direction) < 0:
            new_direction = new_direction + 360

        return new_direction

    @staticmethod
    def tilt_adjust_by_height(new_tilt, tile_down_limit, tilt_upper_limit):
        if new_tilt < tile_down_limit:
            new_tilt = tile_down_limit
        elif new_tilt > tilt_upper_limit:
            new_tilt = tilt_upper_limit
        return new_tilt

    @staticmethod
    def adjust_tilt_by_rule(new_tilt, height):
        if height < 0:
            raise Exception("高度信息错误:" + str(height))
        if height < 20:
            new_tilt = weightchange.tilt_adjust_by_height(new_tilt, 3, 10)
        elif 20 <= height < 30:
            new_tilt = weightchange.tilt_adjust_by_height(new_tilt, 5, 12)
        elif 30 <= height < 40:
            new_tilt = weightchange.tilt_adjust_by_height(new_tilt, 8, 15)
        elif 40 <= height < 50:
            new_tilt = weightchange.tilt_adjust_by_height(new_tilt, 12, 20)
        elif 50 <= height < 60:
            new_tilt = weightchange.tilt_adjust_by_height(new_tilt, 15, 30)
        else:
            new_tilt = weightchange.tilt_adjust_by_height(new_tilt, 20, 35)
        return new_tilt

    @staticmethod
    def get_new_down_tilt(height, down_point_distance):
        angle_radian = down_point_distance * 1000 / height
        angle_degree = math.degrees(round(math.atan(angle_radian), 2))
        return round(90 - angle_degree, 2)

    @staticmethod
    def get_center_angle(end_angle, start_angle, buffer):
        if abs(end_angle - start_angle) > 90:
            if end_angle + buffer < 360:
                return round(end_angle + buffer, 2)
            else:
                return round(buffer - (360 - end_angle), 2)
        else:
            return round(start_angle + buffer, 2)

    # @staticmethod
    # def get_new_direction(center_angle, clock_wise_angle, anti_clock_wise_angle):
    #     if clock_wise_angle >= anti_clock_wise_angle:
    #         new_center_angle = center_angle - (45 - anti_clock_wise_angle)
    #         if new_center_angle < 0:
    #             new_center_angle = 360 + new_center_angle
    #     else:
    #         new_center_angle = center_angle + (45 - clock_wise_angle)
    #         if new_center_angle > 360:
    #             new_center_angle = new_center_angle - 360
    #     return new_center_angle

    # @staticmethod
    # def get_normal_direction(angle, start_angle, end_angle, center_angle, buffer):
    #     """"
    #         判断这个点是否在法线的顺时针方向,并且给出法线角度和法线坐标
    #     """
    #     clockwise = None
    #     if abs(end_angle - start_angle) > 90:
    #         # 判断点是否在法线的顺时针方向
    #         if end_angle + buffer < 360:
    #             # center_angle = end_angle + buffer
    #             if angle is not None:
    #                 clockwise = False if end_angle <= angle <= center_angle else True
    #         else:
    #             # center_angle = buffer - (360 - end_angle)
    #             if angle is not None:
    #                 clockwise = True if start_angle >= angle >= center_angle else False
    #     else:
    #         # center_angle = start_angle + buffer
    #         if angle is not None:
    #             clockwise = True if center_angle <= angle <= end_angle else False
    #
    #     return clockwise

    @staticmethod
    def calculate_proper_point(points, sum_weight):

        weight_lats = []
        weight_lons = []
        for p in points:
            weight = p[0]
            lat = p[1]
            lon = p[2]
            weight_lat = (weight / sum_weight) * lat
            weight_lon = (weight / sum_weight) * lon
            weight_lats.append(weight_lat)
            weight_lons.append(weight_lon)
        return sum(weight_lats), sum(weight_lons)

    def get_proper_points(self):
        self.common_file_df = self.common_file_df[self.common_file_df['是否大于20G'] == '是']
        tqdm.pandas(desc='计算新的方位角和下倾角')
        self.common_file_df[
            ["起始角度", "终止角度", '理论方位角', '调整后方位角', '理论下倾角', '调整后下倾角', '权重和', '优化纬度',
             '优化经度']] = self.common_file_df.progress_apply(
            WeightChange.get_proper_point_by_node,
            axis=1, args=(self.cloud_file_df, self.cover_distance), result_type="expand")
        self.common_file_df['调整后方位角'] = self.common_file_df['调整后方位角'].astype('float').map("{:.4f}".format)
        self.common_file_df.to_csv(self.output_path, index=False, encoding='utf-8-sig')

        self.check_valid(self.common_file_df)

    def check_valid(self, common_file_df):
        """
            1.每个扇区之间夹角60，不能重叠
        """
        common_file_df['方位角'] = common_file_df['方位角'].astype(float)
        common_file_df['调整后方位角'] = common_file_df['调整后方位角'].astype(float)
        common_file_df['按站优化后的方位角'] = None
        direction_adj_result = pd.DataFrame(columns=common_file_df.columns)
        site_number = common_file_df['物理点编号'].unique().tolist()
        bar = tqdm(site_number)
        bar.set_description("检查重叠覆盖,再次调整方位角")
        for site in bar:
            # 1.如果只有一个扇区需要调整，直接跳过
            co_sites = common_file_df[common_file_df['物理点编号'] == site]
            if len(co_sites) == 1:
                direction_adj_result = pd.merge(direction_adj_result, co_sites, how='outer')
                continue
            # 如果当前调整后的方位角相隔都超过60,后面流程不在进行
            if self.check_directions_valid(co_sites['调整后方位角'].tolist(), 60) is True:
                try:
                    direction_adj_result = pd.merge(direction_adj_result, co_sites, how='outer')
                except Exception as e:
                    print()
                continue
            # 2.如果调整后的法线之间相差60度，那么不需要调整,如果超过60度,那么按照覆盖更多的权重点的原则，
            #   选择调整或者不调整扇区
            possible_direction_list = []
            for direction, new_direction, in zip(co_sites['方位角'], co_sites['调整后方位角']):
                direction_list = [str(direction) + ",O", str(new_direction) + ",N"]
                possible_direction_list.append(direction_list)
            direction_tuple = tuple(possible_direction_list)
            result = list(itertools.product(*direction_tuple))
            # 二维列表去重，先转成tuple,然后去重
            result = list(set(tuple(t) for t in result))
            biggest_site_sum_weight = 0
            usable_directions = list()
            # 倒序遍历
            for i in range(len(result) - 1, -1, -1):
                directions = result[i]
                # 如果这种方案的所有下倾角都满足之间夹角大于60度，那么检查权重和
                # 权重和最大方案胜出
                if self.check_directions_valid(directions, 60):
                    site_sum_weight = self.get_after_sum_weight(directions, co_sites, self.cover_distance)
                    if site_sum_weight > biggest_site_sum_weight:
                        usable_directions = list(directions)
            # 没有调整方案均不行，保持不变
            if len(usable_directions) == 0:
                co_sites['按站优化后的方位角'] = co_sites['方位角'].tolist()
                co_sites['按站优化后的方位角'] = co_sites['按站优化后的方位角'].astype(object)
                direction_adj_result = pd.merge(direction_adj_result, co_sites, how='outer')
                continue
            for i in range(len(usable_directions)):
                usable_directions[i] = usable_directions[i].split(",")[0]
            co_sites['按站优化后的方位角'] = usable_directions
            co_sites['按站优化后的方位角'] = co_sites['按站优化后的方位角'].astype('object')
            direction_adj_result = pd.merge(direction_adj_result, co_sites, how='outer')

        direction_adj_result.to_csv("C:\\Users\\No.1\\Desktop\\teleccom\\result1.csv", index=False,
                                    encoding='utf-8-sig')

    def get_after_sum_weight(self, directions, co_sites, cover_distance):
        site_sum_weight = 0
        for direction in directions:
            splits = direction.split(",")
            direction = splits[0]
            pos = splits[1]
            if pos == 'O':
                site_row = co_sites[co_sites['方位角'] == float(direction)]
            else:
                site_row = co_sites[co_sites['调整后方位角'] == float(direction)]
            row = site_row.iloc[0]
            # start_angle = row['起始角度']
            # end_angle = row['终止角度']
            start_angle, end_angle = gutils.get_rad_by_direction(direction)

            match_node_list, cell_sum_weight,match_nodes_names = weightchange.get_match_points(row, self.cloud_file_df, cover_distance,
                                                                             start_angle,
                                                                             end_angle)
            site_sum_weight = site_sum_weight + cell_sum_weight
        return site_sum_weight

    def check_directions_valid(self, directions, threshold):
        for i in range(0, len(directions)):
            # item0 = float(directions[i].split(".")[0])
            item0 = float(directions[i].split(",")[0]) if isinstance(directions[i], str) else directions[i]
            for j in range(i + 1, len(directions)):
                item1 = float(directions[j].split(",")[0]) if isinstance(directions[j], str) else directions[j]
                if abs(item0 - item1) < threshold:
                    return False
        return True


if __name__ == "__main__":
    common_file_path = "C:\\Users\\No.1\\Desktop\\teleccom\\5G小区工参-温州衢州三类四类(1).csv"
    cloud_file_path = "C:\\Users\\No.1\\Desktop\\teleccom\\云勘数据-温州衢州三类四类(1).csv"
    output_path = "C:\\Users\\No.1\\Desktop\\teleccom\\result.csv"
    weightchange = WeightChange(common_file_path, cloud_file_path, output_path, 0.8)
    # df = pd.read_csv(output_path)
    # weightchange.check_valid(df)
    weightchange.get_proper_points()
    # df = pd.read_csv(output_path)
    #weightchange.check_valid(df)
    # list1 = [1, 2, 3, 4]
    # list2 = [5, 6, 7, 8]
    # list3 = [7, 9, 10, 2]
    # tuple = (list1,list2,list3)
    # itertools.product()
    # print(list(itertools.product(*tuple)))
    # result = [x * y  for x, y in zip(list1, list2)]
    # print(result)

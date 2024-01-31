EMPTY_VALUE = "NULL"
END = "END"
QUERY = "查询"
RETURN_CODE = "RETCODE"
COMMAND = "命令"
MESSAGE = "报文"
G5_CELL_IDENTITY = 'NR小区标识'
G4_CELL_IDENTITY = '本地小区标识'


LST_NRCELLALGOSWITCH = ['网元', 'NR小区标识', 'NSA DC开关', '语音策略开关', ' 系统间业务移动性算法开关', ' 邻区自配置开关',
                        ' 异频切换算法开关', ' VoNR开关', ' ROHC头压缩开关', ' ROHC子协议开关', ' 终端节能开关',
                        ' INACTIVE策略开关', '测量策略开关', '负载均衡算法开关', ' 基于RFSP的算法开关', ' 视频直播开关',
                        '网络切片算法开关', ' CloudX业务开关', ' 定位业务开关', ' 切换兼容性开关', ' 终端辅助信息处理开关',
                        '高速专属策略开关', ' ROHC模式', '加速开关', ' FWA算法开关', ' 流程开关', '重配消息传输间隔(毫秒)',
                        '面向企业客户的业务开关', '无线准入控制算法开关', ' 业务功能开关', '异频切换AI优化开关', ' NR-DC开关',
                        ' 多频算法开关', ' 邻区信息控制开关', ' 同频切换算法开关', ' 多频智选模式', '同频切换开关', '同频协同切换模式']

LST_GNODEBFUNCTION = ['网元', 'gNodeB功能名称', '引用的应用标识', 'gNodeB标识', 'gNodeB标识长度(比特)', '用户标签', '网元资源模型版本', '产品版本']

LST_NRDUCELL = ['网元', 'NR DU小区标识', 'NR DU小区名称', '双工模式', '小区标识', '物理小区标识', '频带', '上行频点', '下行频点',
                '上行带宽', '下行带宽', '小区半径(米)', '子载波间隔(KHz)', '循环前缀长度', '时隙配比', '时隙结构', 'RAN通知区域标识',
                'LampSite小区标识', '跟踪区域标识',
                'TA偏移量', '小区管理状态', 'SSB频域位置描述方式', 'SSB频域位置', 'SSB周期(毫秒)', 'SIB1周期(毫秒)',
                'NR DU小区组网模式', '系统消息配置标识', '根序列逻辑索引', 'PRACH频域起始位置', '高速小区标识', '辅助小区指示',
                'SMTC持续时间(毫秒)', 'SMTC周期(毫秒)', '附加频带', 'SSB子载波间隔(KHz)', '客户化带宽配置标识', '客户化下行带宽',
                '客户化上行带宽', '上行闭塞RB个数偏置', '对端时隙配比', 'SSB时域位置', '小区禁止状态',
                '部署位置', 'IAB节点标识']
LST_NRCELLINTERFHOMEAGRP_INTERFREQHOMEASGROUPID_0 = ['网元', 'NR小区标识', '异频切换测量参数组标识', '异频测量事件时间迟滞(毫秒)',
                                                     '异频测量事件幅度迟滞(0.5dB)',
                                                     '异频A1A2时间迟滞(毫秒)', '异频A1A2幅度迟滞(0.5dB)',
                                                     '基于频率优先级的异频切换A2 RSRP门限(dBm)', '基于频率优先级的异频切换A1 RSRP门限(dBm)',
                                                     '基于覆盖的异频A5 RSRP触发门限1(dBm)', '基于覆盖的异频A5 RSRP触发门限2(dBm)',
                                                     '基于覆盖的异频A2 RSRP触发门限(dBm)', '基于覆盖的异频A1 RSRP触发门限(dBm)',
                                                     '基于频率优先级的异频切换A4 RSRP门限(dBm)',
                                                     '基于MLB的异频A4 RSRP门限(dBm)', '运营商专用优先级异频切换A4 RSRP门限(dBm)',
                                                     '基于业务的异频切换A4 RSRP门限(dBm)', '基于覆盖的异频RSRQ门限(0.5dB)',
                                                     '基于覆盖的异频A2 RSRQ触发门限(0.5dB)', '基于覆盖的异频A1 RSRQ触发门限(0.5dB)',
                                                     '基于干扰的异频切换A3 RSRP偏置(0.5dB)', '基于干扰的异频切换RSRP门限(dBm)',
                                                     '基于SSB SINR的异频切换A1门限(0.5dB)', '基于SSB SINR的异频切换A2门限(0.5dB)',
                                                     '基于A3异频切换的A2 RSRP触发门限(dBm)', '基于A3异频切换的A1 RSRP触发门限(dBm)',
                                                     '异频切换A3偏置(0.5dB)', '基于上行覆盖的异频A5 RSRP触发门限1(dBm)',
                                                     '高速用户A2门限偏置(dB)', '基于MBS兴趣指示的异频切换A5 RSRP触发门限2(dBm)',
                                                     '基于覆盖的异频切换A5 SINR门限2(0.5dB)', '异频盲重定向A2 SINR门限(0.5dB)',
                                                     '特殊终端基于频率优先级切换的A1 RSRP门限(dBm)', '特殊终端基于频率优先级切换的A2 RSRP门限(dBm)',
                                                     '特殊终端基于频率优先级切换的A4 RSRP门限(dBm)', '基于干扰隔离的异频A5 RSRP触发门限1(dBm)']

LST_NRCELLINTERFHOMEAGRP_INTERFREQHOMEASGROUPID_2 = LST_NRCELLINTERFHOMEAGRP_INTERFREQHOMEASGROUPID_0

LST_NRINTERRATHOPARAM = ['网元', 'NR小区标识',
                         '切换方式开关',
                         'EPS FB保护定时器(100毫秒)', '异系统切换触发事件类型', 'EPS FB模式', 'EPS FB测量保护定时器(100毫秒)', '下行资源比',
                         'EPS FB等待多频点B1测量报告定时器时长(10毫秒)']
LST_NRCELLINTERRHOMEAGRP_INTERRATHOMEASGROUPID_0 = ['网元', 'NR小区标识', '异系统切换测量参数组标识', '异系统切换A1 RSRP门限(dBm)',
                                                    '异系统切换A2 RSRP门限(dBm)', '异系统切换A1A2幅度迟滞(0.5dB)',
                                                    '异系统切换A1A2时间迟滞(毫秒)', '基于覆盖的切换至E-UTRAN盲A2 RSRP门限(dBm)',
                                                    '基于覆盖的切换至E-UTRAN B2 RSRP门限1(dBm)',
                                                    'VoNR/EPS FB自适应A2 RSRP门限(dBm)', 'VoNR/EPS FB自适应A2事件时间迟滞(毫秒)',
                                                    '异系统切换A2 RSRQ门限(0.5dB)', '异系统切换A1 RSRQ门限(0.5dB)',
                                                    '基于覆盖的切换至E-UTRAN盲A2 RSRQ门限(0.5dB)',
                                                    '基于上行SINR的切换至E-UTRAN B2 RSRP门限1(dBm)']
LST_NRCELLINTERRHOMEAGRP_INTERRATHOMEASGROUPID_1 = ['网元', 'NR小区标识', '异系统切换测量参数组标识', '异系统切换A1 RSRP门限(dBm)',
                                                    '异系统切换A2 RSRP门限(dBm)', '异系统切换A1A2幅度迟滞(0.5dB)',
                                                    '异系统切换A1A2时间迟滞(毫秒)', '基于覆盖的切换至E-UTRAN盲A2 RSRP门限(dBm)',
                                                    '基于覆盖的切换至E-UTRAN B2 RSRP门限1(dBm)',
                                                    'VoNR/EPS FB自适应A2 RSRP门限(dBm)', 'VoNR/EPS FB自适应A2事件时间迟滞(毫秒)',
                                                    '异系统切换A2 RSRQ门限(0.5dB)', '异系统切换A1 RSRQ门限(0.5dB)',
                                                    '基于覆盖的切换至E-UTRAN盲A2 RSRQ门限(0.5dB)',
                                                    '基于上行SINR的切换至E-UTRAN B2 RSRP门限1(dBm)']
LST_NRCELLINTERRHOMEAGRP_INTERRATHOMEASGROUPID_2 = ['网元', 'NR小区标识', '异系统切换测量参数组标识', '异系统切换A1 RSRP门限(dBm)',
                                                    '异系统切换A2 RSRP门限(dBm)', '异系统切换A1A2幅度迟滞(0.5dB)',
                                                    '异系统切换A1A2时间迟滞(毫秒)', '基于覆盖的切换至E-UTRAN盲A2 RSRP门限(dBm)',
                                                    '基于覆盖的切换至E-UTRAN B2 RSRP门限1(dBm)',
                                                    'VoNR/EPS FB自适应A2 RSRP门限(dBm)', 'VoNR/EPS FB自适应A2事件时间迟滞(毫秒)',
                                                    '异系统切换A2 RSRQ门限(0.5dB)', '异系统切换A1 RSRQ门限(0.5dB)',
                                                    '基于覆盖的切换至E-UTRAN盲A2 RSRQ门限(0.5dB)',
                                                    '基于上行SINR的切换至E-UTRAN B2 RSRP门限1(dBm)']
LST_NRCELLHOEUTRANMEAGRP_INTERRHOTOEUTRANMEASGRPID_0 = ['网元', 'NR小区标识', '异系统切换至E-UTRAN测量参数组标识', '基于覆盖的切换B1 RSRP门限(dBm)',
                                                        '基于覆盖的切换B1B2幅度迟滞(0.5dB)', '基于覆盖的切换B1B2时间迟滞(毫秒)',
                                                        'EPSFB B1 RSRP门限(dBm)', 'EPSFB B1幅度迟滞(0.5dB)',
                                                        'EPSFB B1时间迟滞(毫秒)', 'LNR载波关断B1 RSRP门限(dBm)',
                                                        '网络架构优选的RSRP触发门限(dBm)', '基于覆盖的切换B1 RSRQ门限(0.5dB)',
                                                        'EPSFB B1 RSRQ门限(0.5dB)']
LST_NRCELLHOEUTRANMEAGRP_INTERRHOTOEUTRANMEASGRPID_1 = ['网元', 'NR小区标识', '异系统切换至E-UTRAN测量参数组标识', '基于覆盖的切换B1 RSRP门限(dBm)',
                                                        '基于覆盖的切换B1B2幅度迟滞(0.5dB)', '基于覆盖的切换B1B2时间迟滞(毫秒)',
                                                        'EPSFB B1 RSRP门限(dBm)', 'EPSFB B1幅度迟滞(0.5dB)',
                                                        'EPSFB B1时间迟滞(毫秒)', 'LNR载波关断B1 RSRP门限(dBm)',
                                                        '网络架构优选的RSRP触发门限(dBm)', '基于覆盖的切换B1 RSRQ门限(0.5dB)',
                                                        'EPSFB B1 RSRQ门限(0.5dB)']
LST_NRCELLHOEUTRANMEAGRP_INTERRHOTOEUTRANMEASGRPID_2 = ['网元', 'NR小区标识', '异系统切换至E-UTRAN测量参数组标识', '基于覆盖的切换B1 RSRP门限(dBm)',
                                                        '基于覆盖的切换B1B2幅度迟滞(0.5dB)', '基于覆盖的切换B1B2时间迟滞(毫秒)',
                                                        'EPSFB B1 RSRP门限(dBm)', 'EPSFB B1幅度迟滞(0.5dB)',
                                                        'EPSFB B1时间迟滞(毫秒)', 'LNR载波关断B1 RSRP门限(dBm)',
                                                        '网络架构优选的RSRP触发门限(dBm)', '基于覆盖的切换B1 RSRQ门限(0.5dB)',
                                                        'EPSFB B1 RSRQ门限(0.5dB)']

LST_NRDUCELLSRSMEAS = ['网元', 'NR DU小区标识', 'NSA TDM功控触发SINR幅度迟滞(0.1dB)',
                       'NSA TDM功控触发SINR门限(0.1dB)', 'SRS TA测量开关',
                       ' NSA 上行回落到LTE SINR迟滞(0.1dB)', 'NSA 上行回落到LTE SINR门限(0.1dB)',
                       'Hyper Cell内TRP间切换的RSRP差值(0.5dB)', 'NSA上行路径选择SINR高门限(0.1dB)',
                       'NSA上行路径选择SINR低门限(0.1dB)', 'NSA分流用户上行路径选择SINR门限(0.1dB)',
                       'NSA上行路径选择SINR幅度迟滞(0.1dB)', 'NSA上行路径选择SINR时间迟滞(100毫秒)',
                       'NSA上行路径变更至LTE速率比', 'NSA上行路径变更至NR速率比', 'NSA上行小包返回NR后惩罚时长(秒)',
                       'NSA 上行回落到LTE SINR时间迟滞(100毫秒)', 'NSA上行回落到LTE SINR优化开关',
                       'UL ROHC的SINR门限(0.1dB)', 'UL ROHC的SINR幅度迟滞(0.1dB)',
                       'DMM TRP选择RSRP差值门限(dB)', '上行SRS测量值使用开关', 'SRS干扰门限(dB)',
                       'NR迁移到E-UTRAN的上行SINR低门限(0.1dB)', 'E-UTRAN迁移到NR的SINR高门限(0.1dB)',
                       'SRS TA异常保护门限(Ts)', 'SRS均衡前信干噪比低门限(0.2dB)', 'SRS测量优化策略',
                       ' SRS RSRP异常门限(dB)', 'DMRS TA的SINR判决门限(dB)', 'SRS和DMRS TA差值门限(Ts)',
                       'SRS测量扩展开关', ' SRS干扰下TA测量优化开关', 'SRS测量优化开关']

LST_NRCELLQCIBEARER_QCI_1 = ['网元', 'NR小区标识', '服务质量等级', '流控参数组标识', 'AM模式PDCP参数组标识', 'UM模式PDCP参数组标识',
                             'RLC模式', 'DRX参数组标识', '异系统切换测量参数组标识', '异系统切换至E-UTRAN测量参数组标识',
                             '同频切换测量参数组标识', '异频切换测量参数组标识', 'NSA DC配置参数组标识',
                             '切换与QoS流程冲突处理策略', '负载均衡算法开关', ' 负载均衡的下行吞吐率门限(千比特/秒)',
                             '负载均衡的上行吞吐率门限(千比特/秒)', '负载均衡的下行缓存数据量(千比特)',
                             '负载均衡的上行BSR数据量(千比特)', '负载均衡的检查时长(秒)', 'NSA用户异频切换测量参数组标识',
                             '低速用户同频切换测量参数组标识', '低速用户异频切换测量参数组标识', 'RedCap用户DRX参数组标识',
                             '业务释放延迟定时器(毫秒)', 'gNodeB频点优先级组标识', 'QCI算法参数组标识']

LST_NRCELLQCIBEARER_QCI_5 = ['网元', 'NR小区标识', '服务质量等级', '流控参数组标识', 'AM模式PDCP参数组标识',
                             'UM模式PDCP参数组标识', 'RLC模式', 'DRX参数组标识', '异系统切换测量参数组标识',
                             '异系统切换至E-UTRAN测量参数组标识', '同频切换测量参数组标识', '异频切换测量参数组标识',
                             'NSA DC配置参数组标识', '切换与QoS流程冲突处理策略', '负载均衡算法开关',
                             ' 负载均衡的下行吞吐率门限(千比特/秒)', '负载均衡的上行吞吐率门限(千比特/秒)',
                             '负载均衡的下行缓存数据量(千比特)', '负载均衡的上行BSR数据量(千比特)', '负载均衡的检查时长(秒)',
                             'NSA用户异频切换测量参数组标识', '低速用户同频切换测量参数组标识', '低速用户异频切换测量参数组标识',
                             'RedCap用户DRX参数组标识', '业务释放延迟定时器(毫秒)', 'gNodeB频点优先级组标识',
                             'QCI算法参数组标识']
LST_NRCELLQCIBEARER_QCI_9 = ['网元', 'NR小区标识', '服务质量等级', '流控参数组标识', 'AM模式PDCP参数组标识',
                             'UM模式PDCP参数组标识', 'RLC模式', 'DRX参数组标识', '异系统切换测量参数组标识',
                             '异系统切换至E-UTRAN测量参数组标识', '同频切换测量参数组标识', '异频切换测量参数组标识',
                             'NSA DC配置参数组标识', '切换与QoS流程冲突处理策略', '负载均衡算法开关',
                             ' 负载均衡的下行吞吐率门限(千比特/秒)', '负载均衡的上行吞吐率门限(千比特/秒)',
                             '负载均衡的下行缓存数据量(千比特)', '负载均衡的上行BSR数据量(千比特)', '负载均衡的检查时长(秒)',
                             'NSA用户异频切换测量参数组标识', '低速用户同频切换测量参数组标识', '低速用户异频切换测量参数组标识',
                             'RedCap用户DRX参数组标识', '业务释放延迟定时器(毫秒)', 'gNodeB频点优先级组标识',
                             'QCI算法参数组标识']

LST_NRCELLSERVEXP = ['网元', 'NR小区标识', '基于语音质量的异频切换的丢包率门限', '基于业务质量的异频切换A5 RSRP门限2(dBm)',
                     '基于业务质量的异频切换A5 RSRQ门限(0.5dB)', '语音业务丢包率评估周期(秒)', '语音质量恢复的丢包率门限',
                     '基于语音质量的E-UTRAN切换丢包率门限', '基于语音质量的E-UTRAN切换B1 RSRP门限(dBm)',
                     '基于语音质量的E-UTRAN切换B1 RSRQ门限(0.5dB)', 'RRC恢复测量延迟(毫秒)', 'SpeedTurbo用户标识有效时长(秒)',
                     '基于业务质量的异频切换A5 SINR门限(0.5dB)', 'VoNR基于空口超时的EPS FB定时器(100毫秒)']

LST_GNBQCIALGOPARAMGRP = ['网元', 'QCI算法参数组标识', 'QCI算法开关', '业务丢包率评估周期(秒)', '基于业务质量的异频切换的丢包率门限',
                          '基于业务质量的异系统切换的丢包率门限', '业务质量恢复的丢包率门限']
LST_NRCELLRESELCONFIG = ['网元', 'NR小区标识', '最低接收电平(2dBm)', '同频测量启动门限(2dB)', '小区重选迟滞(dB)', '小区重选优先级',
                         'E-UTRAN小区重选定时器时长(秒)', '非同频测量RSRP触发门限(2dB)', '服务频点低优先级RSRP重选门限(2dB)',
                         '小区重选子优先级', 'SSB合并门限', '用于平均的SSB个数', 'UE最大发射功率(dBm)', '非同频测量RSRQ触发门限(dB)',
                         '服务频点低优先级RSRQ重选门限(dB)', 'SIB可选信元指示', ' UE移动状态评估周期', 'UE进入中速状态重选次数门限',
                         'UE进入高速状态重选次数门限', '中速UE额外迟滞值', '高速UE额外迟滞值', '中速UE重选时间比例因子', '高速UE重选时间比例因子',
                         'RRM测量放松低速用户RSRP差值门限', 'RRM测量放松低速用户判决定时器', 'RRM测量放松非边缘用户判决RSRP门限(2dB)']

LST_NRCELLFREQRELATION = ['网元', 'NR小区标识', 'SSB频域位置', '频带', '子载波间隔(KHz)', '小区重选优先级', '最低接收电平(2dBm)',
                          '高优先级重选门限(2dB)', '低优先级重选门限(2dB)', '频率偏置(dB)', '连接态频率优先级', '连接态频率偏置(dB)',
                          '流量优先级', 'SSB频域位置描述方式', 'SMTC周期(毫秒)', 'SMTC持续时间(毫秒)', '附加频带', '测量激活标识',
                          '小区重选子优先级', 'UE最大发射功率(dBm)', '同步DAPS切换标识', '频点干扰状态', '高优先级重选RSRQ门限(dB)',
                          '低优先级重选RSRQ门限(dB)', '最低接收信号质量(dB)', '音视频质量的频点优先级', '基于干扰的频率优先级',
                          '异频切换触发事件类型', '聚合属性', ' 异频周期MR测量类型', 'SMTC偏置(毫秒)', '周期MR层', '高速标识',
                          '频点控制开关', ' ANR指示', 'Idle态MLB释放比例', '盲重定向优先级', '自动NR频点关系的RSRP门限(dBm)',
                          'Idle态MLB释放比例']

LST_NRCELLEUTRANNFREQ = ['网元', 'NR小区标识', '下行E-UTRAN频点', 'E-UTRAN频点高优先级重选门限(2dB)', 'E-UTRAN频点低优先级重选门限(2dB)',
                         'E-UTRAN频点重选优先级', '连接态频率偏置(dB)', '测量带宽', '最低接收电平(2dBm)', '连接态频率优先级',
                         'E-UTRAN频点重选子优先级', 'VoLTE优先级', '聚合属性', ' 测量激活标识', '最大发射功率(dBm)',
                         'NSA PCC频率优先级', '频点干扰标识', 'E-UTRAN高优先级重选RSRQ门限(dB)', 'E-UTRAN低优先级重选RSRQ门限(dB)',
                         '最低接收信号质量(dB)', '频点关系属性', '高速标识', '测量类型', '频点控制开关', ' EPS FB的B1事件RSRP门限(dBm)',
                         '自动EUTRAN频点关系的RSRP门限(dBm)']
LST_NRDUCELLINTRFIDENT = ['网元', 'NR DU小区标识', '干扰识别方式', '上行干扰自动检测门限偏置(dB)', '上行干扰频段调度判决偏置(dB)',
                          '信道测量控制开关', ' SRS SINR门限(dB)', '上行干扰偏置(dB)', '上行干扰门限(dBm)', '干扰优化方式',
                          ' 非干扰段频谱效率加权系数', '干扰段1频谱效率加权系数', '干扰段2频谱效率加权系数', '上行干扰差值门限(dB)',
                          '下行小区级干扰避让策略', '上行干扰避让Slot配置', '下行干扰识别偏置(dB)', '上行SRS干扰差值门限(0.5dB)',
                          '上行阻塞干扰避让模式', '上行干扰隔离模式', '上行调度干扰避让SINR门限(dB)', '上行用户级干扰避让优化方式',
                          '语音下行干扰占比门限', '上行干扰检测门限(dBm)', '合并增益权重', '极致IRC算法开关', '极致IRC干扰门限(dBm)',
                          '极致IRC上行调度干扰门限(dBm)']
LST_NRCELLINTRAFHOMEAGRP_INTRAFREQHOMEASGROUPID_0 = ['网元', 'NR小区标识', '同频切换测量参数组标识', '同频切换的A3偏置(0.5dB)',
                                                     '同频切换的A3幅度迟滞(0.5dB)', '同频切换的A3时间迟滞(毫秒)',
                                                     '同频条件切换的候选邻区A3偏置(0.5dB)', '异构组网同频A3偏置(0.5dB)',
                                                     '室内外交叠区A3偏置(0.5dB)', '同频切换覆盖扩展的A3偏置(0.5dB)']
LST_NRCELLINTRAFHOMEAGRP_INTRAFREQHOMEASGROUPID_2 = ['网元', 'NR小区标识', '同频切换测量参数组标识', '同频切换的A3偏置(0.5dB)',
                                                     '同频切换的A3幅度迟滞(0.5dB)', '同频切换的A3时间迟滞(毫秒)',
                                                     '同频条件切换的候选邻区A3偏置(0.5dB)', '异构组网同频A3偏置(0.5dB)',
                                                     '室内外交叠区A3偏置(0.5dB)', '同频切换覆盖扩展的A3偏置(0.5dB)']
# =====================================================================================================================================


LST_CELL = ['本地小区标识', '小区名称', 'Csg 指示', '上行循环前缀长度', '下行循环前缀长度', 'NB-IoT小区指示', '覆盖等级类型',
            '频带', '上行频点配置指示', '上行频点', '下行频点', '上行带宽', '下行带宽', '小区标识', '物理小区标识', '附加频谱散射',
            '小区激活状态', '小区闭塞优先级', '小区闭塞执行时长(分)', '小区双工模式', '上下行子帧配比', '特殊子帧配比',
            'SSP6下行导频时隙模式', '小区主备模式', '服务小区偏置(dB)', '服务小区频率偏置(dB)', '根序列索引', '高速小区指示',
            '前导格式', '小区半径(米)', '客户化带宽配置指示', '客户化上行实际带宽(0.1兆赫兹)', '客户化下行实际带宽(0.1兆赫兹)',
            'UE最大允许发射功率配置指示', 'UE最大允许发射功率(dBm)', '多RRU共小区指示', '多RRU共小区模式', 'CPRI_E接口压缩比率',
            'CPRI压缩', ' SFN小区物理小区数量', '小区级参考信号端口数', '小区发送和接收模式', '小区参考信号天线端口映射', '用户标签',
            '工作模式', '运营商共享组索引', '服务小区同频RAN共享指示', '服务小区同频ANR指示', '小区起始覆盖位置(米)', '专有小区标识',
            '下行闭塞RB个数', 'SFN主小区标签', '多小区共享模式', ' 辅框小区SFN自动恢复时间(小时)', '压缩带宽控制干扰模式',
            '上行闭塞RB个数偏置', '超高速小区根序列索引']

LST_CELLSEL = ['本地小区标识', '最低接收电平(2dBm)', '最低接收电平偏置(2dB)', '最低接入信号质量(dB)', '最小接收信号接收质量偏置值配置指示',
               '最小接收信号接收质量偏置值(dB)', 'CE最低接收电平(2dBm)', 'CE最低接入信号质量(dB)', 'CE ModeB模式最低接入信号质量(dB)',
               'CE ModeB模式最低接收电平(2dBm)', 'NB-IoT UE小区选择功率偏置值(dB)']

LST_CELLRESEL = ['网元', '本地小区标识', '小区重选迟滞值(dB)', '速度相关重选参数配置指示', 'UE移动状态评估周期(秒)', '判断进入正常移动状态的时间附加迟滞(秒)',
                 'UE进入中速移动状态的小区重选次数', '判断进入高速移动状态的小区改变次数', '中速移动状态UE的Qhyst额外迟滞值(dB)',
                 '高速移动状态UE的Qhyst额外迟滞值(dB)', '异频/异系统测量启动门限配置指示', '异频/异系统测量启动门限(2dB)', '服务频点低优先级重选门限(2dB)',
                 '小区重选优先级', '最低接收电平(2dBm)', '重选UE最大允许发射功率配置指示', 'UE最大允许发射功率(dBm)', '同频测量门限配置指示',
                 '同频测量启动门限(2dB)', '测量带宽配置指示', '测量带宽(兆赫兹)', 'EUTRAN小区重选时间(秒)', '速率状态比例因子配置指示',
                 '中速移动状态UE的EUTRAN小区重选时间比例因子', '高速移动状态UE的EUTRAN小区重选时间比例因子', '同频邻区配置信息',
                 '同频邻区双发射天线配置指示', '同频RSRQ测量启动门限(dB)', '异频/异系统RSRQ测量启动门限(dB)', '服务频点低优先级RSRQ重选门限配置指示',
                 '服务频点低优先级RSRQ重选门限(dB)', '同频重选小区最小接收信号质量配置指示', '同频重选小区最小接收信号质量(dB)',
                 'NB-IoT同频重选时间(秒)', 'NB-IoT异频重选时间(秒)', 'CE EUTRAN小区重选时间(秒)', 'eMTC小区重选优先级',
                 'NB-IoT UE同频小区重选功率偏置值(dB)', 'CE Mode A模式最低接入信号质量(dB)', 'CE Mode B模式最低接入信号质量(dB)',
                 'CE Mode A模式最低接收电平(2dBm)', 'CE Mode B模式最低接收电平(2dBm)', 'NB-IoT小区重选宽松监测测量门限(dB)',
                 'NB-IoT连接态同频测量门限(dBm)', 'NB-IoT连接态异频测量门限(dBm)', 'NB-IoT连接态测量宽松门限(dB)',
                 'eMTC小区重选宽松监测测量门限(dB)']

LST_ENODEBFUNCTION = ['网元', 'eNodeB名称', '引用的应用标识', 'eNodeB标识', '用户标签', '网元资源模型版本', '产品版本', '基站模式']

LST_EUTRANINTERNFREQ = ['网元', '本地小区标识', '下行频点', '上行频点配置指示', '上行频点', '异频频点小区重选优先级配置指示', '异频频点小区重选优先级',
                        'EUTRAN异频重选时间(秒)', '速度相关重选参数配置指示', '中速移动状态UE的EUTRAN小区重选时间比例因子',
                        '高速移动状态UE的EUTRAN小区重选时间比例因子', '测量带宽', '频率偏置(dB)', '异频频点高优先级重选门限(2dB)',
                        '异频频点低优先级重选门限(2dB)', '最低接收电平(2dBm)', '最大发射功率指示', '最大发射功率(dBm)', '异频邻区配置信息',
                        '本地小区异频邻区双发射天线配置指示', '异频切换触发事件类型', '异频频点RSRQ高优先级重选门限(dB)', '异频频点RSRQ低优先级重选门限(dB)',
                        '最小接收信号质量配置指示', '最小接收信号质量(dB)', '连接态频率优先级', '负载均衡目标频点标识', '基于频率优先级的切换测量标志位',
                        'Idle态MLB释放比例(%)', '负载平衡频点优先级', '下行频率偏移', '上行频率偏移', '连接态频率偏置(dB)', '测量频率优先级',
                        '基于覆盖的异频切换RSRP门限偏置(dB)', '异频负载均衡RSRP门限偏置(dB)', '主频段指示', '异频相邻频点RAN共享指示', '异频频点高速指示',
                        'ANR指示', 'Voip优先级', '数据业务优先级', 'VoLTE切换目标频点指示', '低效用户负载平衡目标频点标识', 'MLB异频切换触发事件类型',
                        '移动性目标频点指示', 'MLB异频频谱效率比例', '基于SNR的用户选择模式', '上行业务负载平衡目标频点标识', '上行业务切换优先级',
                        'MLB异频A3偏置(0.5dB)', '基于业务的异频切换RSRP门限偏置(dB)', '基于业务的异频切换RSRQ门限偏置(0.5dB)', '负载平衡频点上行优先级',
                        '异频负载平衡下行PRB偏置(%)', '异频负载平衡上行PRB偏置(%)', 'ANR的邻区个数', '测量性能要求', '异频低效负载均衡RSRP门限偏置(dB)',
                        '异频低效负载均衡RSRQ门限偏置(0.5dB)', '语音质量的异频切换目标频点指示', 'Idle态eMTC UE MLB释放比例(%)', '异频CIO调整范围配置指示',
                        '异频CIO调整范围最小值(dB)', '异频CIO调整范围最大值(dB)', '异频4T频点标识', '频率优先级切换的测量优先级', 'eMTC异频频点小区重选优先级',
                        'NB-IoT UE异频小区重选功率偏置值(dB)', '异频切换A5门限1 RSRP偏置(dB)', '异频切换A5门限1 RSRQ偏置(0.5dB)',
                        '异频周期测量报告频点组标识', '异频重定向控制开关', 'NB-IoT UE异频重定向功率偏置值(dB)', 'CE Mode A模式最低接入信号质量(dB)',
                        'CE Mode B模式最低接入信号质量(dB)', 'CE Mode A模式最低接收电平(2dBm)', 'CE Mode B模式最低接收电平(2dBm)',
                        '基于覆盖的VoLTE异频切换A5门限1 RSRP偏置(dB)', '基于覆盖的VoLTE异频切换A5门限2 RSRP偏置(dB)',
                        '基于A3的异频切换的服务小区RSRP偏置(dB)', '基于覆盖的异频切换NSA DC用户服务小区RSRP偏置(dB)', '聚合属性',
                        ' 基于频率优先级的切换A4门限RSRP偏置(dB)', 'Idle态MLB释放比例', '异频负载平衡下行PRB偏置', '异频负载平衡上行PRB偏置',
                        'Idle态eMTCUEMLB释放比例']

LST_ENODEBALGOSWITCH = ['网元', '切换算法开关', '切换方式开关', '下行ICIC算法开关', 'ANR算法开关', '重定向算法开关', '下行组包优化开关', '天线校正时间开关', 'TPE功能开关',
                        '基于SPID选择PLMN算法开关', 'PIM开关', '上行频域ICIC开关', 'LCS功能开关', 'TRM算法开关', 'PCI冲突告警开关', '节能开关',
                        'RIM流程开关', '网络共享场景下的ANR开关', '语音质量追踪算法开关', '用户数抢占算法开关', '多运营商控制开关', '基于BBU协作的算法开关',
                        '运营商定制算法开关', '切换信令优化开关', '兼容性控制开关', '盲邻区优化开关', '通过eCoordinator支持RIM流程开关', 'EUTRAN支持VoIP能力开关',
                        'CA算法开关', 'MLB算法开关', '切换公共优化开关', '重载网络性能优化开关', '调度优化开关', 'PRACH时域错开开关',
                        '高速移动根序列循环移位开关', '丢包统计功能开关', '邻区排序开关', '一体化基站开关', '根序列冲突检测开关', '智能优化算法开关',
                        '业务切换多目标频点开关', '软失效自愈开关', 'PCI冲突检测开关', 'CA负载平衡算法开关', '上行提前调度优化开关', '一体化基站多APN开关',
                        '系统时钟跳变重建小区处理开关', '端到端语音质量评估算法开关', '组呼调度算法开关', 'TL频段帧偏置开关', '过滤重复RRCConReq消息延长开关',
                        '快速增强型主载波锚点开关', '切换时SCell增加盲配小区开关', '软劈裂资源复用算法开关', 'IoT系统时钟跳变小区复位开关', 'CA算法扩展开关',
                        '上行资源管理优化开关', 'LTE抢占NB开关', '干扰优化开关', 'V2X算法开关', 'MFBI自动配置开关', '时钟检测增强开关', 'RRU定位开关',
                        '时钟检测增强灵敏度', '硬件能力扩展开关', '通道校正算法开关', '虚拟栅格算法开关']

LST_CELLALGOSWITCH = ['网元', '本地小区标识', '语音重定向开关', '随机接入控制算法开关', 'SRS算法开关', ' PUCCH算法开关', ' MTC用户拥塞控制开关',
                      'AQM算法开关', ' CQI调整算法开关', ' MTC用户省电控制开关', '动态调压开关', ' 准入负载控制开关', '负载平衡算法开关',
                      ' Turbo Receiver开关', 'NAICS算法开关', '下行功控算法开关', '上行功控算法开关', ' 上行IC开关', ' BF算法开关',
                      '下行调度开关', '上行调度开关', 'DACQ增强开关', ' RAN共享模式开关', '基于频率优先级的切换算法开关', 'MUBF算法开关',
                      ' 基于距离的切换开关', '接入禁止算法开关', 'SFN上行调度开关', 'SFN下行调度开关', 'IRC算法开关', ' 动态DRX特性开关',
                      ' 高移动性触发的空闲态控制开关', '规避干扰开关', ' GL功率共享开关', 'Eicic开关', '上行峰值PUCCH资源开关', '下行CoMP算法开关',
                      'PSIC算法开关', ' 负载平衡切换方式', ' 上行CoMP开关', '天线校正算法开关', ' 动态频谱共享开关', ' SFN基于负载的自适应算法开关',
                      'PUSCH IRC算法开关', ' 加速用户保障开关', '重选优先级自适应开关', 'ANR功能开关', ' SFN算法开关', 'PRACH干扰抑制开关',
                      'MIMO增强特性开关', ' 干扰随机化算法开关', '直放站开关', ' 多频点优先级控制开关', ' HARQ算法开关', ' 基于覆盖的异频切换模式',
                      'LTE系统UTC时间广播开关', '小区调度策略开关', ' SFN小区内上行Comp开关', ' 低速用户异频切换开关', 'Relay开关',
                      '异频定向切换开关', '功率降额选择开关', '检测算法开关', 'PucchIRC增强', '动态接入禁止算法开关', ' CRE开关',
                      '低效用户负载平衡算法开关', ' 切换允许开关', ' 邻区分类管理开关', '基于特定PCI组的策略开关', '小区级互调干扰抑制开关',
                      'PRACH联合接收开关', 'FeICIC算法开关', '协调AMC算法开关', 'RRU与UE对应关系开关', '高速优化开关', '差异化调度开关',
                      '一键通QoS保障开关', 'SRS和PUCCH资源分配增强开关', '语音业务UE不活动定时器开关', '上行联合接收天线数组合开关',
                      ' 虚拟天线映射相位因子开关', ' 小区ANR算法开关', ' 下行256QAM算法开关', '负载均衡自动分组配置开关', ' 载波聚合自动分组配置开关',
                      ' 归属关系自规划开关', '下行小区覆盖增强特性开关', ' 上行调度扩展开关', ' 用户数据压缩算法开关', 'VoLTE算法开关',
                      '语音解密自纠错开关', ' Deprioritisation发送指示', 'CMAS开关', 'MFBI算法开关', ' PCI冲突上报开关', 'MRO算法开关',
                      '运营商资源组共享开关', '小区能力恢复开关', ' 移动性负载平衡算法增强开关', '业务负载平衡开关', ' MTC开关',
                      '上行干扰协调调度算法开关', ' FCS工作模式', ' 视频优化开关', '基于SPID的切换开关', 'D-MIMO算法开关', '上行速率控制模式',
                      '速率控制算法开关', ' CRS干扰消除算法开关', '增强通道校正开关', 'NB-IoT小区算法开关', ' 多运营商连接态频率优先级开关',
                      '无SRS辅载波BF算法开关', '专有用户算法开关', ' MIMO用户级自适应Pa调整开关', '非标带宽算法开关', '覆盖增强模式切换开关',
                      ' 协同算法开关', ' 测量优化算法开关', '频点分层开关', 'eMIMO开关', ' ROHC开关', 'MCPTT开关', '上行单用户MIMO算法开关',
                      '高速用户异系统切换开关', '紧急呼叫半静态调度开关', '上行干扰协调调度RB占比(%)', '上行干扰协调调度VoLTE路损门限(dB)',
                      '定位特性开关', ' DTX识别算法开关', ' 频谱接入系统算法开关', '基于QCI的动态AMBR开关', '上行高阶CoMP开关',
                      ' 基于Uu口的V2X业务算法开关', ' 下行调度扩展开关', 'MPMU维测开关', ' 垂直劈裂算法开关', ' RRC重建数据转发开关',
                      '小带宽优化开关', '空闲态eDRX开关', '上行干扰协调调度RB占比']

LST_CELLALGOEXTSWITCH = ['网元', '本地小区标识', 'NB-IoT小区级算法扩展开关', '天选算法开关', ' 测速开关', '上行覆盖增强开关', 'WTTx算法开关',
                         ' WTTx MU-MIMO开关', '切换允许开关', ' 波束天线扩展开关', ' 重载性能优化开关', '下行调度增强开关', 'LNR智能载波关断',
                         'ANR优化开关', 'LTE In-band异频部署开关', '上行调度增强开关', 'LTE带宽兼容性优化开关', ' 测量优化算法扩展开关',
                         ' 邻区算法开关', ' 运营商功能开关', ' 小区强化学习寻优开关', ' 小区能力恢复时间段']

LST_CELLHOPARACFG = ['网元', '本地小区标识', '异频异系统盲切换 A1A2事件 RSRP门限(dBm)', '异频异系统盲切换 A1A2事件 RSRQ门限(0.5dB)',
                     '高速门限(千米/小时)', '切换方式开关', ' SRVCC切换优化开关', ' 上行质量差切换MCS门限', '上行质量差切换IBLER门限(%)',
                     '速度评估周期', '速度评估周期内切换次数', '到UTRAN CSFB测量报告处理模式', 'CSFB测量报告等待定时器(毫秒)', '切换算法开关',
                     '快速UE速率评估次数', '切换时处理UE不活动定时器开关', ' 高铁休眠用户数门限', '低速用户选择保护定时器(分)',
                     '高速小区切换入保护定时器(0.5秒)', 'Flash SRVCC开关', '上行弱覆盖路损门限(dB)', '上行弱覆盖SINR门限(0.1dB)',
                     '异系统语音质量切换的QCI1丢包率门限(%)', '语音质量丢包评估周期(秒)', '语音业务切换测量报告延迟定时器(毫秒)', '语音质量切换算法开关',
                     ' 高速用户判决方式', '振铃消息校验开关', 'SRVCC测量报告延迟定时器(秒)', '异频语音质量切换的QCI1丢包率门限(%)',
                     '语音质量恢复的QCI1丢包率门限(%)', '基于覆盖系统内测量时长(秒)', '异系统空口切换失败重试次数', 'E-UTRAN RSRP高层滤波系数',
                     'E-UTRAN RSRQ高层滤波系数', 'CE模式A紧急盲重定向A1A2 RSRP触发门限(dBm)', 'CE模式A紧急盲重定向A1A2 RSRQ触发门限(0.5dB)',
                     '异系统测量报告延迟定时器(毫秒)', '基于业务的E-UTRAN切换至NR测量定时器(秒)', '基于CQI的异频切换门限',
                     'VoLTE用户NR切换延迟定时器(100毫秒)', '频率优先级站内切换下行PRB门限(%)', '频率优先级站内切换上行PRB门限(%)',
                     '基于业务的NR B1测量报告等待定时器(秒)', '上行链路质差增强切换频谱效率门限(0.1bit/s/Hz)', 'NR B1快速切换门限偏置(dB)',
                     '工程测试盲切换模式', 'NR资源优化切换入保护定时器(秒)', 'Gap模式类型', ' 专有Gap模式类型', 'NR测量报告等待定时器(100毫秒)',
                     'NR测量报告处理模式', '上行质量差切换IBLER门限', '异系统语音质量切换的QCI1丢包率门限', '异频语音质量切换的QCI1丢包率门限',
                     '语音质量恢复的QCI1丢包率门限', '频率优先级站内切换下行PRB门限', '频率优先级站内切换上行PRB门限']

LST_INTRAFREQHOGROUP_INTRAFREQHOGROUPID_0 = ['网元', '本地小区标识', '同频切换参数组ID', '同频切换幅度迟滞(0.5dB)', '同频切换偏置(0.5dB)',
                                             '同频切换时间迟滞', '高速用户同频切换时间迟滞(毫秒)', 'CE同频切换A2 RSRP触发门限(dBm)',
                                             'ModeA调整A1门限(dBm)', 'ModeA调整A2门限(dBm)', 'ModeB调整A2门限(dBm)',
                                             'NC调整A1门限(dBm)',
                                             'CE模式A同频切换A2 RSRQ触发门限(0.5dB)', 'eMTC用户切换A3时间迟滞(毫秒)']

LST_INTRAFREQHOGROUP_INTRAFREQHOGROUPID_2 = LST_INTRAFREQHOGROUP_INTRAFREQHOGROUPID_0

LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_0 = ['网元', '本地小区标识', '异频切换参数组ID', '异频A1A2幅度迟滞(0.5dB)', '异频A1A2时间迟滞(毫秒)',
                                             '基于A4A5异频A1 RSRP触发门限(dBm)', '基于A4A5异频A1 RSRQ触发门限(0.5dB)',
                                             '基于A4A5异频A2 RSRP触发门限(dBm)', '基于A4A5的异频A2 RSRQ触发门限(0.5dB)',
                                             '异频切换幅度迟滞(0.5dB)', '基于覆盖的异频RSRP触发门限(dBm)', '基于覆盖的异频RSRQ触发门限(0.5dB)',
                                             '异频切换时间迟滞(毫秒)', '基于负载的异频RSRP触发门限(dBm)', '基于负载的异频RSRQ触发门限(0.5dB)',
                                             '基于频率优先级的异频A1 RSRP触发门限(dBm)', '基于频率优先级的异频A1 RSRQ触发门限(0.5dB)',
                                             '异频A3偏置(0.5dB)', '基于A3的异频A1 RSRP触发门限(dBm)', '基于A3的异频A2 RSRP触发门限(dBm)',
                                             '基于频率优先级的异频A2 RSRP触发门限(dBm)', '基于频率优先级的异频A2 RSRQ触发门限(0.5dB)',
                                             '基于负载平衡的A1A2 RSRP触发门限(dBm)', '异频切换A5 RSRP门限1(dBm)',
                                             '异频切换A5 RSRQ门限1(0.5dB)',
                                             '基于业务请求的异频RSRP触发门限(dBm)', '基于业务请求的异频RSRQ触发门限(0.5dB)',
                                             '基于MLB的异频A5门限1 RSRP门限(dBm)', '基于MLB的异频A5门限1 RSRQ门限(0.5dB)', '上行质量差切换A4偏置',
                                             '基于A3的异频A1 RSRQ触发门限(0.5dB)', '基于A3的异频A2 RSRQ触发门限(0.5dB)',
                                             '上行大业务负载平衡的异频RSRP触发门限(dBm)', '上行大业务负载平衡的异频RSRQ触发门限(0.5dB)',
                                             'CE 异频A1 RSRP触发门限(dBm)', 'CE 异频A2 RSRP触发门限(dBm)', 'MM负载分流的异频RSRP触发门限(dBm)',
                                             'CE模式异频A4 RSRP触发门限(dBm)', 'CE模式A A3异频切换A2 RSRP触发门限(dBm)',
                                             'CE模式A A3异频切换A2 RSRQ触发门限(0.5dB)', 'CE模式A异频切换A2 RSRQ触发门限(0.5dB)',
                                             'CE模式A异频切换A4 RSRQ触发门限(0.5dB)', '异频切换A3时间迟滞(毫秒)',
                                             '基于业务的异频切换A2 RSRP触发门限(dBm)',
                                             '基于业务的异频切换A2 RSRQ触发门限(0.5dB)', '异频切换A3的RSRQ偏置(0.5dB)', '异频切换A3幅度迟滞(0.5dB)',
                                             'A3异频切换的A1A2测量触发类型', 'A4A5异频切换的A1A2测量触发类型', '异频切换A3测量报告上报类型',
                                             '异频切换A4A5测量报告上报类型']
LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_1 = LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_0
LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_2 = LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_0

LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_0 = ['网元', '本地小区标识', 'E-UTRAN切换至NR的切换参数组ID', 'NR切换B1/B2事件幅度迟滞(0.5dB)',
                                               'NR切换B1/B2事件时间迟滞(毫秒)', '基于覆盖的E-UTRAN切换至NR B1事件RSRP触发门限(dBm)',
                                               '基于业务的E-UTRAN切换至NR B1事件RSRP触发门限(dBm)', 'NSA DC用户SA NR切换无Gap测量B1事件时间迟滞',
                                               '基于业务的E-UTRAN切换至NR B1事件RSRQ触发门限(0.5dB)',
                                               '基于覆盖的E-UTRAN切换至NR B1事件RSRQ触发门限(0.5dB)',
                                               'Fast Return B1事件时间迟滞(毫秒)']
LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_1 = LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_0
LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_2 = LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_0

LST_CELLQCIPARA_QCI_1 = ['网元', '本地小区标识', '服务质量等级', '异频切换参数组ID', '异系统CDMA2000HRPD切换参数组ID',
                         '异系统切换公共参数组ID', '异系统GERAN切换参数组ID', '异系统UTRAN切换参数组ID', '同频切换参数组ID',
                         'DRX参数组ID', 'SRI周期', ' RLF定时器与常量参数配置指示', 'RLF定时器与常量参数组ID',
                         '业务延迟释放时长(毫秒)', '切换配置QCI优先级', '负载平衡QCI参数组ID', '预调度参数组ID',
                         'DRX特定的QCI优先级', 'QCI算法开关', ' QCI与EUTRAN异频频点关系ID', 'QCI与UTRAN异系统频点关系ID',
                         'QCI与GERAN异系统频点关系ID', 'eMTC模式A覆盖等级1的DRX参数组ID', 'eMTC模式B覆盖等级3的DRX参数组ID',
                         '业务标识', '下行AMBR限速因子', 'QCI AMBR限速标识', '上行AMBR限速因子', '拥塞门限(%)',
                         '切换业务准入门限(%)', '下行IBLER目标值初始值(%)', 'SINR校正算法的IBLER目标值(%)', 'eMTC SRI周期',
                         '最大排队时长(秒)', '非受限用户控制速率(kbps)', 'QCI PDCCH SINR偏移量(0.1dB)',
                         'NACK CQI调整量降低值(0.1dB)', '覆盖远点用户上行路损门限', 'E-UTRAN切换至NR的切换参数组ID',
                         'QCI级触发TTI Bundling的SINR门限(dB)', '低时延标识', 'NSA DC默认承载模式',
                         '低时延远点用户预调度优化门限(0.1dB)', '低时延用户SR调度最小数据量(比特)', 'NSA DC GERAN切换参数组ID',
                         'NSA DC异频切换参数组ID', 'NSA DC异系统切换公共参数组ID', 'NSA DC同频切换参数组ID',
                         'NSA DC UTRAN切换参数组ID', 'NSA DC优化开关', ' NSA DC DRX参数组ID', '上行HARQ最大传输次数',
                         'eMTC模式A覆盖等级0的DRX参数组ID', 'eMTC模式B覆盖等级2的DRX参数组ID', 'NSA DC QCI参数组ID',
                         '最大载波数', '基于业务的重选目标下行频点', '系统频点优先级组ID', 'NSA DC系统频点优先级组ID',
                         'NR SCG频点优先级组ID', '拥塞门限', '切换业务准入门限', '下行IBLER目标值初始值', 'SINR校正算法的IBLER目标值']
LST_CELLQCIPARA_QCI_9 = LST_CELLQCIPARA_QCI_1

G5_COMMAND_COLS_LIST = [LST_NRDUCELL, LST_GNODEBFUNCTION, LST_NRCELLALGOSWITCH,
                        LST_NRCELLINTERFHOMEAGRP_INTERFREQHOMEASGROUPID_0,
                        LST_NRCELLINTERFHOMEAGRP_INTERFREQHOMEASGROUPID_2,
                        LST_NRINTERRATHOPARAM, LST_NRCELLINTERRHOMEAGRP_INTERRATHOMEASGROUPID_0,
                        LST_NRCELLINTERRHOMEAGRP_INTERRATHOMEASGROUPID_1,
                        LST_NRCELLINTERRHOMEAGRP_INTERRATHOMEASGROUPID_2,
                        LST_NRCELLHOEUTRANMEAGRP_INTERRHOTOEUTRANMEASGRPID_0,
                        LST_NRCELLHOEUTRANMEAGRP_INTERRHOTOEUTRANMEASGRPID_1,
                        LST_NRCELLHOEUTRANMEAGRP_INTERRHOTOEUTRANMEASGRPID_2,
                        LST_NRDUCELLSRSMEAS,
                        LST_NRCELLQCIBEARER_QCI_1, LST_NRCELLQCIBEARER_QCI_5, LST_NRCELLQCIBEARER_QCI_9,
                        LST_NRCELLSERVEXP, LST_GNBQCIALGOPARAMGRP, LST_NRCELLRESELCONFIG, LST_NRCELLFREQRELATION,
                        LST_NRCELLEUTRANNFREQ, LST_NRDUCELLINTRFIDENT,
                        LST_NRCELLINTRAFHOMEAGRP_INTRAFREQHOMEASGROUPID_0,
                        LST_NRCELLINTRAFHOMEAGRP_INTRAFREQHOMEASGROUPID_2]

G4_COMMAND_COLS_LIST = [LST_CELLRESEL, LST_ENODEBFUNCTION, LST_CELL, LST_CELLSEL,
                        LST_EUTRANINTERNFREQ,
                        LST_INTRAFREQHOGROUP_INTRAFREQHOGROUPID_0,
                        LST_INTRAFREQHOGROUP_INTRAFREQHOGROUPID_2,
                        LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_0,
                        LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_1,
                        LST_INTERFREQHOGROUP_INTERFREQHOGROUPID_2,
                        LST_ENODEBALGOSWITCH, LST_CELLALGOSWITCH, LST_CELLALGOEXTSWITCH,
                        LST_CELLHOPARACFG,
                        LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_0,
                        LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_1,
                        LST_INTERRATHONRPARAMGRP_NRHOPARAMGROUPID_2,
                        LST_CELLQCIPARA_QCI_1, LST_CELLQCIPARA_QCI_9
                        ]
G4_COMMAND_NAME_LIST = ['LST CELLRESEL:;', 'LST ENODEBFUNCTION:;', 'LST CELL:;', 'LST CELLSEL:;',
                        'LST EUTRANINTERNFREQ:;',
                        'LST INTRAFREQHOGROUP:INTRAFREQHOGROUPID=0;',
                        'LST INTRAFREQHOGROUP:INTRAFREQHOGROUPID=2;',
                        'LST INTERFREQHOGROUP:INTERFREQHOGROUPID=0;',
                        'LST INTERFREQHOGROUP:INTERFREQHOGROUPID=1;',
                        'LST INTERFREQHOGROUP:INTERFREQHOGROUPID=2;',
                        'LST ENODEBALGOSWITCH:;',
                        'LST CELLALGOSWITCH:;', 'LST CELLALGOEXTSWITCH:;', 'LST CELLHOPARACFG:;',
                        'LST INTERRATHONRPARAMGRP:NRHOPARAMGROUPID=0;',
                        'LST INTERRATHONRPARAMGRP:NRHOPARAMGROUPID=1;',
                        'LST INTERRATHONRPARAMGRP:NRHOPARAMGROUPID=2;',
                        'LST CELLQCIPARA:QCI=1;',
                        'LST CELLQCIPARA:QCI=9;']

G5_COMMAND_NAME_LIST = ['LST NRDUCELL:;', 'LST GNODEBFUNCTION:;', 'LST NRCELLALGOSWITCH:;',
                        'LST NRCELLINTERFHOMEAGRP:INTERFREQHOMEASGROUPID=0;',
                        'LST NRCELLINTERFHOMEAGRP:INTERFREQHOMEASGROUPID=2;',
                        'LST NRINTERRATHOPARAM:;',
                        'LST NRCELLINTERRHOMEAGRP:INTERRATHOMEASGROUPID=0;',
                        'LST NRCELLINTERRHOMEAGRP:INTERRATHOMEASGROUPID=1;',
                        'LST NRCELLINTERRHOMEAGRP:INTERRATHOMEASGROUPID=2;',
                        'LST NRCELLHOEUTRANMEAGRP:INTERRHOTOEUTRANMEASGRPID=0;',
                        'LST NRCELLHOEUTRANMEAGRP:INTERRHOTOEUTRANMEASGRPID=1;',
                        'LST NRCELLHOEUTRANMEAGRP:INTERRHOTOEUTRANMEASGRPID=2;',
                        'LST NRDUCELLSRSMEAS:;',
                        'LST NRCELLQCIBEARER:QCI=1;',
                        'LST NRCELLQCIBEARER:QCI=5;',
                        'LST NRCELLQCIBEARER:QCI=9;',
                        'LST NRCELLSERVEXP:;', 'LST GNBQCIALGOPARAMGRP:;', 'LST NRCELLRESELCONFIG:;',
                        'LST NRCELLFREQRELATION:;', 'LST NRCELLEUTRANNFREQ:;', 'LST NRDUCELLINTRFIDENT:;',
                        'LST NRCELLINTRAFHOMEAGRP:INTRAFREQHOMEASGROUPID=0;',
                        'LST NRCELLINTRAFHOMEAGRP:INTRAFREQHOMEASGROUPID=2;']

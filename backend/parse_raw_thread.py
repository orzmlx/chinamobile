# -*- coding:utf-8 -*-
import logging
import traceback
from datetime import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from model.data_watcher import DataWatcher
from model.signal_message import message
from processor.process_util import ProcessUtils

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.INFO)


class ParseRawThread(QThread):
    handle = -1
    valueChanged = pyqtSignal(int)
    finished = pyqtSignal(message)
    total_file_number = pyqtSignal(int)

    def __init__(self,
                 work_path: str = None,
                 raw_path: str = None,
                 watcher: DataWatcher = None,
                 system: str = '5G',
                 config_path: str = None,
                 *args, **kwargs):
        super(ParseRawThread, self).__init__(*args, **kwargs)
        self.work_dir = work_path
        self.raw_path = raw_path
        self.system = system
        self.dataWatcher = watcher
        self.config_path = config_path
        now = datetime.now()
        self.date = now.strftime('%Y%m%d')

    def run(self):
        try:
            if self.dataWatcher.work_dir is None or len(self.dataWatcher.work_dir) == 0:
                raise Exception("没有设置工作路径")
            if self.dataWatcher.manufacturer is None or self.dataWatcher.system is None:
                raise Exception("请先设置厂商")
            if self.dataWatcher.huawei_command_path is None and self.dataWatcher.manufacturer == '华为':
                raise Exception("没有导入华为命令")
            # 解压所有的文件,然后提取所有的txt文件，复制到工作文件夹
            processor = ProcessUtils.get_processor(watcher=self.dataWatcher)
            raw_logs = processor.before_parse_raw_data(self.dataWatcher)
            # 向前端更新总的文件数量
            self.total_file_number.emit(len(raw_logs))
            for index, log in enumerate(raw_logs):
                processor.parse_raw_data(log, dataWatcher=self.dataWatcher)
                self.valueChanged.emit(index + 1)
            self.finished.emit(message(2, "成功"))
            logging.info('==============解析原始Log文件完成' + '==============')
        except Exception as e:
            traceback.print_exc()  # 打印错误栈
            logging.error(e)
            self.finished.emit(message(-1, str(e)))


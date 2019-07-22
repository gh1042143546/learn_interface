"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from Utils.config import Config,LOG_PATH
class Logger(object):
    def __init__(self,logger_name='InterFace'):
        #创建logger，如果参数为空则返回root logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO) #设置logger日志等级
        c = Config().get('log')
        self.log_file_name = c["file_name"]
        self.backup_count = c['backup']
        # 日志输出级别
        self.console_output_level = c.get('console_level')
        self.file_output_level = c.get('file_level')
        #日志格式
        pattern = c.get('pattern')
        self.formatter = logging.Formatter(pattern)
    def get_logger(self):
        if not self.logger.handlers:  # 避免重复日志
            #创建handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            #为handler指定输出格式
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            #为logger添加的日志处理器
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()

if __name__ == "__main__":
    logger = Logger().get_logger()
    logger.info('dd')


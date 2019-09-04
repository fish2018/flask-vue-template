import logging,os
from app.config import APP_ENV

class Log:
    '''
    日志工具类，使用示例:
    from flask import current_app
    current_app.logger.info('yyyy')
    '''
    def __init__(self):
        # 创建日志目录
        log_path = APP_ENV.LOGPATH
        log_name = APP_ENV.LOGNAME + '.log'
        log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_path
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # 日志文件路径
        log_file = log_path + os.sep + log_name
        # 日志处理器
        handler = logging.FileHandler(log_file, encoding='UTF-8')
        # 日志格式
        logging_format = logging.Formatter(APP_ENV.LOGFORMAT)
        handler.setFormatter(logging_format)
        self.handler = handler

    def init_app(self,app):
        # 通过log.init_app(app)加载到Flask实例中
        app.logger.setLevel(APP_ENV.LOGLEVEL)
        app.logger.addHandler(self.handler)


log = Log()

import os
import time

# Dev config file
basedir = os.path.abspath(os.path.dirname(__file__))

class DbConf:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACH_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    # 安全配置
    CSRF_ENABLED = True
    SECRET_KEY = 'jklklsadhfjkhwbii9/sdf\sdf'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/PMS?charset=utf8mb4'
    # SQLALCHEMY_ECHO = True


class LogConf:
    LOGPATH = "logs"
    LOGNAME = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    LOGFORMAT = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s"
    LOGLEVEL = "INFO"


class DevelopmentConfig(DbConf,LogConf):
    pass
import os
import time

# Prod config file
basedir = os.path.abspath(os.path.dirname(__file__))

class DbConf:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACH_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    # 安全配置
    CSRF_ENABLED = True
    SECRET_KEY = 'jklklsadhfjkhwbii9/sdf\sdf'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://devops:devopsSunmi666@104.250.34.119:3306/athena_dev?charset=utf8'
    # SQLALCHEMY_ECHO = True


class LogConf:
    LOGPATH = "logs"
    LOGNAME = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    LOGFORMAT = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s"
    LOGLEVEL = "INFO"


class ProductionConfig(DbConf,LogConf):
    pass
"""
user_starter settings
"""
import os
from starter.utils.common import get_conf

############## 路径配置 ##############
# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件路径
CONFIG_PATH = os.path.join(os.path.dirname(BASE_DIR), 'etc/user_starter.ini')

############## 日志配置 ##############
LOGGING = {
    'loggername': 'user_starter',
    'format': '[%(levelname)s] %(asctime)s %(pathname)s %(lineno)s: %(message)s',
    # 等级标准
    # 日常开发调试: debug
    # 关键节点: info
    # 部分合理存在错误: warning
    # 异常,非合理性错误: error
    'level': 'DEBUG',
    'log_path': '/opt/log/user_starter',
}

############## 连接配置 ##############
USER_MYSQL = '{engine}://{user}:{password}@{host}:{port}/{db}'.format(
    engine='mysql+pymysql',
    host=get_conf('user_mysql', 'host', CONFIG_PATH),
    port=int(get_conf('user_mysql', 'port', CONFIG_PATH)),
    db="usercenter",
    user=get_conf('user_mysql', 'user', CONFIG_PATH),
    password=get_conf('user_mysql', 'password', CONFIG_PATH),
)
MYSQL = '{engine}://{user}:{password}@{host}:{port}/{db}'.format(
    engine='mysql+pymysql',
    host=get_conf('mysql', 'host', CONFIG_PATH),
    port=get_conf('mysql', 'port', CONFIG_PATH),
    db="nms_db",
    user=get_conf('mysql', 'user', CONFIG_PATH),
    password=get_conf('mysql', 'password', CONFIG_PATH),
)
print(USER_MYSQL)
print(MYSQL)
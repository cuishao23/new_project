import logging
import sys
from starter.config import common
from starter.utils.log import init_logger
from starter.user_import import init_importer, export_data

logger = logging.getLogger(common.LOGGING['loggername'])

# starter模块初始化
def init():
    try:
        # 初始化日志模块
        init_logger()
        logger.info('user_starter start up!')

        # 数据导入模块
        # init_importer()

        # 数据导出模块
        export_data()

    except Exception as e:
        logger.error('user_starter init error! %s' % e)
        print("e=%s"%e)

        sys.exit(-1)

if __name__ == '__main__':
    init()

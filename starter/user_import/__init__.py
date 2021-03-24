import logging
import xlwt
import openpyxl
import os
from starter.config.common import LOGGING
from starter.dao.mysql import user_session_scope, new_session_scope
from starter.dao.user_mysql import *
from starter.dao.new_mysql import add_g100_user_infos, get_new_user_infos

logger = logging.getLogger(LOGGING['loggername'])


def init_importer():
    '''
    user原始数据导入
    '''
    logger.info('user importer ...')
    with user_session_scope() as session:
        g100_user_info_list = get_g100_user_list(session)
        with new_session_scope() as session:
            for info in g100_user_info_list:
                add_g100_user_infos(session, info)

    logger.info('user importer ok!')
    print('user importer ok!')

def export_data():
    '''
    :数据导出
    :return: excel
    '''
    try:
        template = {
            'userInfo': {
                'title': ('姓名', '手机号'),
                'field': ('name', 'mobile')
            }
        }

        with new_session_scope() as session:
            user_list = get_new_user_infos(session)

        inspect_result = openpyxl.Workbook()

        sheet = inspect_result.create_sheet('userInfo')
        sheet = inspect_result.active
        for c, name in enumerate(template['userInfo']['title']):
            sheet.cell(1, c+1, name)
        for r, info in enumerate(user_list):
            for c, name in enumerate(template['userInfo']['field']):
                value = info.get(name, '')
                sheet.cell(r + 1, c+1, str(value))
        os.makedirs('/Users/cuixin/Desktop/data', exist_ok=True)
        inspect_result.save('/Users/cuixin/Desktop/data/today.xls')

        logger.info('export_data ok!')
        print('export_data ok!')
    except Exception as e:
        logger.error(e)
        print('export_data error=%s'%e)
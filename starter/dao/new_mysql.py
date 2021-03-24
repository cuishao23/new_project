from starter.dao.mysql.mysql import *


# g100_user
def add_g100_user_infos(session, data):
    '''
    添加g100_user到新表
    '''
    user_info = UserInfo(
        name=data[0],
        mobile=data[1]
    )
    session.add(user_info)

def get_new_user_infos(session):
    '''
    筛选要下载的数据
    '''
    result = session.query(UserInfo.name, UserInfo.mobile).all()

    user_list = []
    for info in result:
        user_list.append({'name': info.name, 'mobile': info.mobile})
    return user_list
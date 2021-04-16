from starter.dao.mysql.mysql import *
from sqlalchemy import and_, or_, func, text
from starter.utils import is_valid_date


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


# def get_new_user_infos(session):
#     '''
#     筛选要下载的数据
#     '''
#     result = session.query(UserInfo.name, UserInfo.mobile).all()[1:10]
#
#     user_list = []
#     for info in result:
#         user_list.append({'name': info.name, 'mobile': info.mobile})
#     return user_list

def get_new_user_infos(session):
    '''
    筛选要下载的数据
    '''
    # result = session.query(UserInfo.name, UserInfo.mobile).all()[0:2]
    #
    # user_list = []
    # for info in result:
    #     user_list.append({'name': info.name, 'mobile': info.mobile})

    # 无参数查询
    sql = '''
        SELECT
          app,
            date_format(FROM_UNIXTIME(move_user_channel.create_time), '%Y-%m') AS '月度',
            COUNT( app ),
            province
        FROM
            move_user_channel 
        LEFT JOIN move_user_info on move_user_channel.uid = move_user_info.uid
        GROUP BY
          app,
            date_format(FROM_UNIXTIME(move_user_channel.create_time), '%Y-%m'),
            province
        ORDER BY
            app ASC,
            date_format(FROM_UNIXTIME(move_user_channel.create_time), '%Y-%m') ASC
    '''
    result = session.execute(text(sql)).fetchall()
    print(type(result))
    print(result)
    user_list = []
    for info in result:
        user_list.append({'user_app': info[0], 'user_month': info[1], 'user_count': info[2], 'user_prince': info[3]})

    return user_list


def get_dec_user_infos(session):
    '''
    拿到要进行手机号dec加密的数据
    '''
    result = session.query(UserInfo.id, UserInfo.mobile).all()
    return result


def update_user_infos(session, data):
    '''
    更新加密unionid
    '''
    if data and data[0]:
        user = session.query(UserInfo).filter(
            UserInfo.id == data[0]).first()
        if user is not None:
            user.mobileid = data[1]

    # def replace_utf8mb4(self, v):
    #     """Replace 4-byte unicode characters by REPLACEMENT CHARACTER"""
    #     import re
    #     # INVALID_UTF8_RE = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
    #     # INVALID_UTF8_RE.sub(u'\uFFFD', v)


def get_user_info(session):
    '''
    筛选要下载的数据
    '''
    # result = session.query(UserInfo.name, UserInfo.mobile).all()[0:2]
    #
    # user_list = []
    # for info in result:
    #     user_list.append({'name': info.name, 'mobile': info.mobile})

    # 无参数查询
    sql = '''
        SELECT
            move_user.id,
            move_user.name,
            move_user.mobile,
            FROM_UNIXTIME( move_user.create_time ),
            move_user_channel.openid,
            move_user_channel.app,
            move_user_channel.session_key,
            move_user_channel.gid,
            move_user_channel.extappid,
            move_user_channel.dist,
            move_user_channel.point,
            move_user_channel.total_point,
            move_user_info.uid,
            move_user_info.role,
            move_user_info.status,
            move_user_info.nickname,
            move_user_info.avatarurl,
            move_user_info.gender,
            move_user_info.country,
            move_user_info.province,
            move_user_info.city,
            move_user_info.id_type,
            move_user_info.id_number,
            move_user_info.address,
            move_user_info.reg_user_id,
            move_user_info.jdid,
            move_user_info.verifytime,
            move_user_info.real_name,
            move_user_info.real_idcard,
            move_user_info.conflict_idcard,
            move_user_info.phone_token,
            move_user_info.token_time,
            move_user_info.validity,
            move_user_info.logindays,
            move_user_info.email,
            move_user_info.birth,
            move_user_info.appid,
            move_user_info.login_type,
            move_user_info.login_id
        FROM
            move_user
            JOIN move_user_channel ON move_user.unionid = move_user_channel.unionid
            JOIN move_user_info ON move_user.id = move_user_info.uid 
        LIMIT 20000,1
    '''
    result = session.execute(text(sql)).fetchall()

    user_list = []

    import emoji
    import re
    for info in result:
        nickname = str(info[15])
        emoji_str = str(emoji.demojize(nickname))
        nickname = re.sub('\?', '', emoji_str).strip()  # 清洗后的数据
        # print(nickname)
        # print(str(info[15]))
        # emoji_str = emoji.demojize(info[15])
        # nickname = re.sub(r':(.*?):', '', emoji_str).strip()  # 清洗后的数据
        user_list.append({'id': info[0], 'name': info[1], 'mobile': info[2], 'create_time': info[3],
                          'openid': info[4], 'app': info[5], 'session_key': info[6], 'gid': info[7],
                          'extappid': info[8], 'dist': info[9], 'point': info[10], 'total_point': info[11],
                          'uid': info[12], 'role': info[13], 'status': info[14], 'nickname': nickname,
                          'avatarurl': info[16],
                          'gender': '男' if info[17] == 1 else '女', 'country': info[18], 'province': info[19],
                          'city': info[20], 'id_type': info[21],
                          'id_number': info[22], 'address': info[23], 'reg_user_id': info[24], 'jdid': info[25],
                          'verifytime': info[26],
                          'real_name': info[27], 'real_idcard': info[28], 'conflict_idcard': info[29],
                          'phone_token': info[30], 'token_time': info[31],
                          'validity': info[32], 'logindays': info[33], 'email': info[34], 'birth': info[35],
                          'appid': info[36],
                          'login_type': info[37], 'login_id': info[38]})

    return user_list


def get_idcard_info(session):
    '''
    拿到身份证号码
    '''
    result = session.query(MoveMember.id, MoveMember.id_number, MoveMember.id_type).all()
    return result

    # user_list = []
    # for info in result:
    #     user_list.append({'id': info.id, 'id_number': info.id_number})
    # return user_list


def update_move_member(session, data):
    '''
    更新加密unionid
    '''
    if data and data[0]:
        user = session.query(MoveMember).filter(
            MoveMember.id_number == data[0]).first()
        if user is not None:
            user.birth = data[1] if is_valid_date(data[1]) else None
            user.gender = data[2]
            user.province = data[3]
            user.city = data[4]
            user.county = data[5]

"""luban数据库请求"""
from starter.dao.mysql.user_mysql import *
from sqlalchemy.sql import func


def get_g100_user_list(session):
    return session.query(
        G100User.name,
        G100User.mobile
    ).all()

def get_dec_t_user(session):
    '''
    拿到要进行手机号dec加密的数据
    '''
    result = session.query(MpmsRegisterMembers.id, MpmsRegisterMembers.mobile).all()
    return result

def update_t_user(session, data):
    '''
    更新加密unionid
    '''
    if data and data[0]:
        user = session.query(MpmsRegisterMembers).filter(
            MpmsRegisterMembers.id == data[0]).first()
        if user is not None:
            user.mobileid = data[1]

def get_dec_tygy_user(session):
    '''
    拿到要进行手机号dec加密的数据
    '''
    result = session.query(TygyUser.id, TygyUser.mobile, TygyUser.unionid).all()
    return result

def update_tygy_user(session, data):
    '''
    更新加密unionid
    '''
    if data and data[0]:
        user = session.query(TygyUser).filter(
            TygyUser.id == data[0]).first()
        if user is not None and data[2] == '':
            user.unionid = data[1]

def get_spark_user(session):
    '''
    拿到要进行手机号dec加密的数据
    '''
    result = session.query(SparkUser.id, SparkUser.mobile).all()
    return result

def update_spark_user(session, data):
    '''
    更新加密unionid
    '''
    if data and data[0]:
        user = session.query(SparkUser).filter(
            SparkUser.id == data[0]).first()
        if user is not None:
            user.unionid = data[1]
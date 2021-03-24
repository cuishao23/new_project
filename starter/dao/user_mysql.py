"""luban数据库请求"""
from starter.dao.mysql.user_mysql import *
from sqlalchemy.sql import func


def get_g100_user_list(session):
    return session.query(
        G100User.name,
        G100User.mobile
    ).all()
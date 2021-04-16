""""new数据库映射"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, SmallInteger, Enum, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'move_user'
    id = Column(Integer, primary_key=True)
    unionid = Column(String(128), primary_key=True)
    name = Column(String(28))
    mobile = Column(String(200))
    mobileid = Column(String(200))
    create_time = Column(Integer)
    id_type = Column(Integer)
    id_number = Column(String(128))


class MoveUserChannel(Base):
    __tablename__ = 'move_user_channel'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    unionid = Column(String(128))
    openid = Column(String(200))
    app = Column(Integer)
    create_time = Column(Integer)
    session_key = Column(String(225))
    token = Column(String(225))
    gid = Column(Integer)
    extappid = Column(String(64))
    dist = Column(Integer)
    point = Column(Integer)
    total_point = Column(Integer)


class MoveUserInfo(Base):
    __tablename__ = 'move_user_info'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    role = Column(Integer)
    status = Column(Integer)
    create_time = Column(Integer)
    nickname = Column(String(255))
    avatarurl = Column(String(255))
    gender = Column(Integer)
    country = Column(String(255))
    province = Column(String(255))
    city = Column(String(255))
    language = Column(String(255))
    id_type = Column(Integer)
    id_number = Column(String(255))
    address = Column(String(255))
    reg_user_id = Column(Integer)
    jdid = Column(Integer)
    verifytime = Column(DateTime)
    real_name = Column(Integer)
    real_idcard = Column(String(128))
    conflict_idcard = Column(String(128))
    phone_token = Column(String(255))
    token_time = Column(DateTime)
    validity = Column(DateTime)
    logindays = Column(Integer)
    email = Column(String(255))
    birth = Column(DateTime)
    appid = Column(Integer)
    login_type = Column(String(64))
    login_id = Column(String(64))
    district_id = Column(String(255))
    street = Column(String(255))


class MoveMember(Base):
    __tablename__ = 'move_member'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    id_type = Column(Integer)
    id_number = Column(String(128))
    birth = Column(DateTime)
    gender = Column(Integer)
    province = Column(String(128))
    city = Column(String(128))
    county = Column(String(128))
    state = Column(Integer)
    status = Column(Integer)
    create_time = Column(Integer)

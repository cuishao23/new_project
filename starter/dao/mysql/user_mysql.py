""""user原始数据库映射"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, SmallInteger, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class G100User(Base):
    __tablename__ = 'g100_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    mobile = Column(String(20))
    unionid = Column(String(20))


class Tuser(Base):
    __tablename__ = 't_user'
    user_id = Column(Integer, primary_key=True)
    mobile = Column(String(20))
    unionid = Column(String(128))


class TygyUser(Base):
    __tablename__ = 'tygy_user'
    id = Column(Integer, primary_key=True)
    mobile = Column(String(20))
    unionid = Column(String(128))


class SparkUser(Base):
    __tablename__ = 'spark_user'
    id = Column(Integer, primary_key=True)
    mobile = Column(Integer)
    unionid = Column(String(128))


class LuyueUser(Base):
    __tablename__ = 'luyue_user'
    id = Column(Integer, primary_key=True)
    login = Column(String(32))
    mobileid = Column(String(200))


class PhysicalEnrollInfo(Base):
    __tablename__ = 'physical_enroll_info'
    id = Column(Integer, primary_key=True)
    phone = Column(String(32))
    unionid = Column(String(200))


class MpmsRegisterMembers(Base):
    __tablename__ = 'mpms_register_members'
    id = Column(Integer, primary_key=True)
    mobile = Column(String(13))
    mobileid = Column(String(128))

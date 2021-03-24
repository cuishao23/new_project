""""user原始数据库映射"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, SmallInteger, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


# 服务域信息
class G100User(Base):
    __tablename__ = 'g100_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    mobile = Column(String(20))
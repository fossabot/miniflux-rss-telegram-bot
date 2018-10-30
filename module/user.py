#coding:utf-8
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    """
    telegarm user table
    """
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    username = Column(String(20))
    password = Column(String(32))


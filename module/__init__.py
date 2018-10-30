#coding:utf-8
# pylint: disable=invalid-name
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .user import Base

# 初始化数据库连接:
Engine = create_engine('sqlite:///test.db')

# 创建DBSession类型:
DBSession = sessionmaker(bind=Engine)

Base.metadata.create_all(Engine)

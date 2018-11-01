# coding:utf-8
# pylint:disable=all
import sys
sys.path.append("..")

import pytest
from help import get_module_function__doc
from telegram.ext import CommandHandler
from tool import bot_function
from client import new_client
from miniflux import Client
from error import UserNotBindError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from module.user import Base, User

engine = create_engine('sqlite:///:memory:', echo=True)
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def test_help():
    ret = get_module_function__doc('command')
    assert isinstance(ret, str)
    assert ret != ''

def test_bind():
    session = DBSession()
    user = User(id='1', username='test', password='123456')
    session.merge(user)
    session.commit()
    session.close()

def test_new_client():
    ret = new_client('1', session=DBSession)
    assert isinstance(ret, Client)

def test_new_client_error():
    with pytest.raises(UserNotBindError):
        ret = new_client('2',session=DBSession)

def test_bot_function():
    @bot_function(0)
    def test():
        """
        """
        pass
    assert isinstance(test,CommandHandler)

def test_run():
    import run

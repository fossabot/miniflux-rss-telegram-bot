# coding:utf-8
# pylint:disable=all
import sys
sys.path.append("..")

import pytest
from help import get_module_function__doc
from telegram.ext import CommandHandler
from fake import *
from command import *
from tool import bot_function
from client import new_client
from constant import *
from miniflux import Client
from error import UserNotBindError


def test_help():
    ret = get_module_function__doc('command')
    assert isinstance(ret, str)
    assert ret != ''

def test_bot_function():
    @bot_function(0)
    def test():
        """test"""
        pass
    assert isinstance(test,CommandHandler)
    # if not, help_doc == ''
    from tool import help_doc
    assert 'test' in help_doc

def test_run():
    import run

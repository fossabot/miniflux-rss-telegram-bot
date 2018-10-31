#coding:utf-8
# pylint:disable=all
import sys
import os
sys.path.append('..')
from tgintegration import BotIntegrationClient
from constant import *
from command import *

botname = os.environ.get('botname')
app_id = os.environ.get('app_id')
app_hash = os.environ.get('app_hash')
_
client = BotIntegrationClient(
    bot_under_test=botname,
    session_name = 'account'
    api_id=app_id,
    api_hash =api_hash,
)


def test_start():
    client.start()
    client.clear_chat() 
    response = client.send_command_await("start")
    assert response.num_messages == 1
    assert response[0].text == start.__doc__.strip()
    client.stop()







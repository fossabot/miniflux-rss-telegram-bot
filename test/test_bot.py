#coding:utf-8
# pylint:disable=all
import sys
sys.path.append('..')
from tgintegration import BotIntegrationClient
from constant import *
from command import *

client = BotIntegrationClient(
    bot_under_test='@bluebirdrss_bot',
    session_name = 'account'
)


def test_start():
    client.start()
    client.clear_chat() 
    response = client.send_command_await("start")
    assert response.num_messages == 1
    assert response[0].text == start.__doc__.strip()
    client.stop()







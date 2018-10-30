#coding:utf-8
import logging
import os 
from telegram.ext import Updater
from telegram.ext import CommandHandler
from command import start,bind,new_user,add_feed,export,discover,get_entries
from error import UserNotBindError

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = os.environ.get('token')
UPDATER = Updater(token=TOKEN)
DISPATCHER = UPDATER.dispatcher

START_HANDLER = CommandHandler('start', start)
BIND_HANDLER = CommandHandler('bind', bind, pass_args=True)
NEW_USER_HANDLER = CommandHandler('new_user',new_user,pass_args=True)
ADD_FEED_HANDLER = CommandHandler('add_feed',add_feed,pass_args=True)
EXPORT_HANDLER = CommandHandler('export',export)
DISCOVER_HANDLER = CommandHandler('discover',discover,pass_args=True)
GET_ENTRIES_HANDLET = CommandHandler('get_entries', get_entries, pass_args=True)

DISPATCHER.add_handler(START_HANDLER)
DISPATCHER.add_handler(BIND_HANDLER)
DISPATCHER.add_handler(NEW_USER_HANDLER)
DISPATCHER.add_handler(ADD_FEED_HANDLER)
DISPATCHER.add_handler(EXPORT_HANDLER)
DISPATCHER.add_handler(DISCOVER_HANDLER)
DISPATCHER.add_handler(GET_ENTRIES_HANDLET)

UPDATER.start_polling()

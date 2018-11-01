#coding:utf-8
import logging
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler, Filters
from command import *
from help import help
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
HELP_HANDLET = CommandHandler('help', help)
IMPORT_HANDLET = MessageHandler(Filters.document, import_feed)

DISPATCHER.add_handler(START_HANDLER)
DISPATCHER.add_handler(BIND_HANDLER)
DISPATCHER.add_handler(NEW_USER_HANDLER)
DISPATCHER.add_handler(ADD_FEED_HANDLER)
DISPATCHER.add_handler(EXPORT_HANDLER)
DISPATCHER.add_handler(DISCOVER_HANDLER)
DISPATCHER.add_handler(GET_ENTRIES_HANDLET)
DISPATCHER.add_handler(HELP_HANDLET)
DISPATCHER.add_handler(me)
DISPATCHER.add_handler(delete_feed)
DISPATCHER.add_handler(get_categories)
DISPATCHER.add_handler(create_category)
DISPATCHER.add_handler(delete_category)
DISPATCHER.add_handler(delete_user)
DISPATCHER.add_handler(IMPORT_HANDLET)

if __name__ == "__main__":
    UPDATER.start_polling()

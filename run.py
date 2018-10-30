#coding:utf-8
import logging
import os 
from telegram.ext import Updater
from telegram.ext import CommandHandler
from constant import ( START_MSG, BIND_OK_MSG, BIND_USAGE_MSG, CREATE_USAGE_MSG,
                       CREATE_OK_MSG, ADD_FEED_USAGE_MSG, ADD_FEED_OK_MSG, NO_BIND_MSG,
                       ID_NO_INT_MSG)
from command import export,discover,get_entries
from error import UserNotBindError
from client import new_client
from module import DBSession
from module.user import User
from config import admin_client
from miniflux import ClientError

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = os.environ.get('token')
UPDATER = Updater(token=TOKEN)
DISPATCHER = UPDATER.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=START_MSG)

def bind(bot, update, args):
    if len(args) != 2:
       bot.send_message(chat_id=update.message.chat_id, text=BIND_USAGE_MSG)
       return
    session = DBSession()
    user = User(id=update.message.chat_id, username=args[0], password=args[1]) 
    session.merge(user)
    session.commit()
    session.close()
    bot.send_message(chat_id=update.message.chat_id, text=BIND_OK_MSG)

def new_user(bot, update, args):
    if len(args) != 2:
       bot.send_message(chat_id=update.message.chat_id, text=CREATE_USAGE_MSG)
       return
    try:
        admin_client.create_user(args[0],args[1], False)    
    except ClientError as e: # pylint: disable=invalid-name
        bot.send_message(chat_id=update.message.chat_id, text=e.get_error_reason())
        return 
    bot.send_message(chat_id=update.message.chat_id, text=CREATE_OK_MSG)
    
def add_feed(bot, update, args):
    if len(args) != 2: 
       bot.send_message(chat_id=update.message.chat_id, text=ADD_FEED_USAGE_MSG)
       return
    if not args[1].isdecimal():
       bot.send_message(chat_id=update.message.chat_id, text=ID_NO_INT_MSG)
       return
    try:
        client = new_client(update.message.chat_id)
    except UserNotBindError as e: # pylint: disable=invalid-name
        bot.send_message(chat_id=update.message.chat_id, text=NO_BIND_MSG)
        return    
    try:
        client.create_feed(args[0], int(args[1]))
    except ClientError as e: # pylint: disable=invalid-name
        bot.send_message(chat_id=update.message.chat_id, text=e.get_error_reason())
        return
    bot.send_message(chat_id=update.message.chat_id, text=ADD_FEED_OK_MSG)

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

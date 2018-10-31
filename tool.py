#coding:utf-8
import functools
from typing import Callable
from module import DBSession
from module.user import User
from error import UserNotBindError 
from client import new_client
from telegram.ext import CommandHandler
from miniflux import ClientError

global help_doc 

help_doc = ''

def bot_function(arg_num=0):
    def decorator(func):
        def wrapper(bot,update,args=[]): 
            if len(args)!=arg_num:
                bot.send_message(chat_id=update.message.chat_id, text=func.__doc__)
                return
            try:
                client = new_client(update.message.chat_id)
            except UserNotBindError: 
                bot.send_message(chat_id=update.message.chat_id, text=NO_BIND_MSG)
                return    
            try:
                func(bot, update, args, client) 
            except ClientError as error:
                bot.send_message(chat_id=update.message.chat_id, text=error.get_error_reason())
                return
        global help_doc
        help_doc = help_doc + func.__doc__
        return CommandHandler(func.__name__,wrapper, pass_args=bool(arg_num))
    return decorator

#codoing:utf-8
import io
import json
import telegram 
from client import new_client
from constant import NO_BIND_MSG, DISCOVER_USAGE_MSG, GET_ENTRIES_USAGE_MSG
from telegram import InputFile
from miniflux import ClientError
def export(bot, update):
    try:
        client = new_client(update.message.chat_id)
    except UserNotBindError:
        bot.send_message(chat_id=update.message.chat_id, text=NO_BIND_MSG)
        return    
    try:
         _ = client.export()
    except ClientError as error: 
        bot.send_message(chat_id=update.message.chat_id, text=error.get_error_reason())
        return
    opml_file = io.BytesIO(bytes(_,'utf-8'))
    bot.send_document(chat_id=update.message.chat_id, document=opml_file, filename="export.opml")
    opml_file.close()

def discover(bot, update, args):
    if len(args) != 1: 
       bot.send_message(chat_id=update.message.chat_id, text=DISCOVER_USAGE_MSG)
       return
    try:
        client = new_client(update.message.chat_id)
    except UserNotBindError:
        bot.send_message(chat_id=update.message.chat_id, text=NO_BIND_MSG)
        return    
    try:
        ret  = client.discover(args[0])
    except ClientError as error: 
        bot.send_message(chat_id=update.message.chat_id, text=error.get_error_reason())
        return
    bot.send_message(chat_id=update.message.chat_id,text="发现成功 订阅地址{}".format(ret[0]['url'])) 

def get_entries(bot, update, args):
    if len(args) != 1: 
       bot.send_message(chat_id=update.message.chat_id, text=GET_ENTRIES_USAGE_MSG)
       return
    try:
        client = new_client(update.message.chat_id)
    except UserNotBindError:
        bot.send_message(chat_id=update.message.chat_id, text=NO_BIND_MSG)
        return    
    try:
        ret  = client.get_entries(limit=args[0])
    except ClientError as error: 
        bot.send_message(chat_id=update.message.chat_id, text=error.get_error_reason())
        return
    for _ in ret['entries']:
        bot.send_message(chat_id=update.message.chat_id,text=_['url'],parse_mode=telegram.ParseMode.HTML)
     

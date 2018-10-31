#coding:utf-8
import inspect
from tool import help_doc

def get_module_function__doc(module):
    module = __import__(module)
    name_func_tuples = inspect.getmembers(module, inspect.isfunction)
    name_func_tuples = [t[1] for t in name_func_tuples if inspect.getmodule(t[1]) == module]
    tmp = ''
    for _ in name_func_tuples:
        tmp = tmp+_.__doc__
    return help_doc+tmp

def help(bot, update): 
    bot.send_message(chat_id=update.message.chat_id, text=get_module_function__doc('command'))

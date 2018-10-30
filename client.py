#coding:utf-8
from module import DBSession
from module.user import User
from error import UserNotBindError
from miniflux import Client
from config import SERBER_ADDR

def new_client(user_id: str) -> Client:
    session = DBSession()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    if user.id == '':
       raise UserNotBindError 
    return Client(SERBER_ADDR,username=user.username, password=user.password)
    
    

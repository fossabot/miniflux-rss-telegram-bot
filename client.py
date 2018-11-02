# coding:utf-8
from error import UserNotBindError
from miniflux import Client
from config import SERBER_ADDR, redis_client

def new_client(user_id: str, session=redis_client) -> Client:
    user = session.get(user_id)
    username,password = user.split()
    if user is None:
       raise UserNotBindError
    return Client(SERBER_ADDR,username=username, password=password)

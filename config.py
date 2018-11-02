#coding:utf-8
import miniflux
import redis
import os

HOST = os.environ.get('host') or '127.0.0.1'

PORT = os.environ.get('port') or '8080'

USERNAME = os.environ.get('username') or 'admin'

PASSWORD  = os.environ.get('password') or '123456'

REDIS_HOST = os.environ.get('redis_host') or '127.0.0.1'
REDIS_PORT = int(os.environ.get('redis_port')) or 6378
REDIS_PW =  os.environ.get('redis_password') or None
# pylint: disable=invalid-name
admin_client = miniflux.Client("http://{host}:{port}".format(\
                                host=HOST,port=PORT), USERNAME, PASSWORD)
redis_client = redis.StrictRedis(host=REDIS_HOST, \
                                 port=REDIS_PORT,password=REDIS_PW,db=0)

SERBER_ADDR = "http://{host}:{port}".format(host=HOST,port=PORT)

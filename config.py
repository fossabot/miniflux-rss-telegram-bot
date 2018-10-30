#coding:utf-8
import miniflux
import os

HOST = os.environ.get('host') or '127.0.0.1'

PORT = os.environ.get('port') or '8080'

USERNAME = os.environ.get('username') or 'admin'

PASSWORD  = os.environ.get('password') or '123456'

# pylint: disable=invalid-name 
admin_client = miniflux.Client("http://{host}:{port}".format(host=HOST,port=PORT), USERNAME, PASSWORD)

SERBER_ADDR = "http://{host}:{port}".format(host=HOST,port=PORT)

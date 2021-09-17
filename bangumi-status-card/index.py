# -*- coding: utf-8 -*-

import os
import logging

from app import build_user_status_card

APP_ID = os.getenv('APP_ID')


# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#    logger = logging.getLogger()
#    logger.info('initializing')


def handler(environ, start_response):
    logging.info(f"environ: \n{environ}")
    request_uri = environ['fc.request_uri']
    logging.info(f"request_uri: {request_uri}")
    remote_addr = environ.get('REMOTE_ADDR')
    logging.info(f"remote_addr: {remote_addr}")
    querys = environ.get('QUERY_STRING').split('&')
    querys_key_value = {}
    for q in querys:
        k_v = q.split('=')
        key = k_v[0]
        value = k_v[1]
        querys_key_value[key] = value
    user_id = querys_key_value.get('User')
    logging.info(f"user_id: {user_id}")

    card_contents = build_user_status_card(
        user_id=user_id,
        app_id=APP_ID).encode('utf8')

    status = '200 OK'
    response_headers = [
        ('Content-type', 'image/svg+xml; charset=utf-8'),
        ('Transfer-Encoding', 'chunked'),
        ('Content-Encoding', 'br')
    ]
    start_response(status, response_headers)

    return [card_contents]

# environ = {'FC_QUALIFIER': 'LATEST',
#            'HOSTNAME': '******',
#            'GPG_KEY': '******',
#            'FC_FUNC_LOG_PATH': '/var/log/fc/',
#            'TERM': 'xterm',
#            'FC_SERVER_CAM_PORT': '10080',
#            'LD_LIBRARY_PATH': '/code/:/code//lib:/usr/local/lib',
#            'accessKeyID': '******',
#            'FC_SERVER_PATH': '/var/fc/runtime/python3',
#            'FC_SERVER_LOG_PATH': '/var/fc/runtime/python3/var/log',
#            'PYTHON_VERSION': '3.6.3',
#            'PATH': '/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
#            'PWD': '/code',
#            'FC_FUNC_CODE_PATH': '/code/',
#            'LANG': 'C.UTF-8',
#            'PYTHON_PIP_VERSION': '9.0.1',
#            'SHLVL': '0',
#            'HOME': '/tmp',
#            'accessKeySecret': '******',
#            'FC_SERVER_PORT': '9000',
#            'securityToken': '******',
#            'FC_SERVER_LOG_LEVEL': 'INFO',
#            'topic': 'status-cards',
#            'SERVER_NAME': '******',
#            'GATEWAY_INTERFACE': 'CGI/1.1',
#            'SERVER_PORT': '9000',
#            'REMOTE_HOST': '',
#            'CONTENT_LENGTH': '0',
#            'SCRIPT_NAME': '',
#            'SERVER_PROTOCOL': 'HTTP/1.1',
#            'SERVER_SOFTWARE': 'WSGIServer/0.2',
#            'PATH_INFO': '/',
#            'REQUEST_METHOD': 'GET',
#            'fc.request_uri': '******',
#            'REMOTE_ADDR': '202.*.*.186',
#            'CONTENT_TYPE': 'text/plain',
#            'HTTP_ACCEPT': '*/*',
#            'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
#            'HTTP_AUTHORIZATION': '******',
#            'HTTP_HOST': '******',
#            'HTTP_ORIGIN': 'https://fcnext.console.aliyun.com',
#            'HTTP_REFERER': 'https://fcnext.console.aliyun.com/',
#            'HTTP_SEC_CH_UA': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
#            'HTTP_SEC_CH_UA_MOBILE': '?0',
#            'HTTP_SEC_CH_UA_PLATFORM': '"Windows"',
#            'HTTP_SEC_FETCH_DEST': 'empty',
#            'HTTP_SEC_FETCH_MODE': 'cors',
#            'HTTP_SEC_FETCH_SITE': 'cross-site',
#            'HTTP_USER': '',
#            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                               'AppleWebKit/537.36 (KHTML, like Gecko) '
#                               'Chrome/93.0.4577.82 Safari/537.36',
#            'HTTP_X_FORWARDED_PROTO': 'https',
#            'fc.context': "< context.FCContext object at 0x7f335a904f60 >",
#            'wsgi.input': "< _io.BufferedReader >",
#            'wsgi.errors': "< _io.TextIOWrapper name = '<stderr>' mode = 'w' encoding = 'UTF-8' >",
#            'wsgi.version': (1, 0),
#            'wsgi.run_once': False,
#            'wsgi.url_scheme': 'http',
#            'wsgi.multithread': True,
#            'wsgi.multiprocess': False,
#            'wsgi.file_wrapper': "<class 'wsgiref.util.FileWrapper'>"
# }

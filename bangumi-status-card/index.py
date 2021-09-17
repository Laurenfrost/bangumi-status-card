# -*- coding: utf-8 -*-

import logging

HELLO_WORLD = b'Hello world!\n'


# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#    logger = logging.getLogger()
#    logger.info('initializing')


def handler(environ, start_response):
    context = environ['fc.context']
    request_uri = environ['fc.request_uri']
    for k, v in environ.items():
        if k.startswith('HTTP_'):
            # process custom request headers
            pass
    # do something here
    with open('template/card.html') as f:
        card_contents = f.read()

    status = '200 OK'
    response_headers = [
        ('Content-type', 'image/svg+xml; charset=utf-8'),
        ('Transfer-Encoding', 'chunked'),
        ('Content-Encoding', 'br')
    ]
    start_response(status, response_headers)

    return [card_contents.encode('utf8')]

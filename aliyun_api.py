# -*- coding:utf-8 -*-
import base64
import datetime
import hashlib
import hmac
import urllib.error
import urllib.parse
import urllib.request
import traceback


def get_current_date():
    date = datetime.datetime.strftime(datetime.datetime.utcnow(), "%a, %d %b %Y %H:%M:%S GMT")
    return date


def to_md5_base64(content_bytes):
    hash = hashlib.md5()
    hash.update(content_bytes)
    return base64.b64encode(hash.digest())


def to_sha1_base64(content_bytes, secret):
    hmacsha1 = hmac.new(secret, content_bytes, hashlib.sha1)
    return base64.b64encode(hmacsha1.digest())


class AliyunApi:

    def __init__(self,ak_id, ak_secret):
        self.ak_id = ak_id
        self.ak_secret = ak_secret

    def post(self, url, body_bytes):
        options = {
            'method': 'POST',
            'headers': {
                'accept': 'application/json',
                'content-type': 'application/json',
                'date':  get_current_date(),
                'authorization': ''
            }
        }
        bodymd5 = to_md5_base64(body_bytes).decode('utf-8')
        urlPath = urllib.parse.urlparse(url)
        if urlPath.query != '':
            urlPath = urlPath.path + "?" + urlPath.query
        else:
            urlPath = urlPath.path
        stringToSign = options['method'] + '\n' + options['headers']['accept'] + '\n' + bodymd5 + '\n' + \
                       options['headers']['content-type'] + '\n' + options['headers']['date'] + '\n' + urlPath
        signature = to_sha1_base64(stringToSign.encode('utf-8'), self.ak_secret.encode('utf-8')).decode('utf-8')
        authHeader = 'Dataplus ' + self.ak_id + ':' + signature
        options['headers']['authorization'] = authHeader
        request = None
        method = options['method']
        if 'GET' == method or 'DELETE' == method:
            request = urllib.request.Request(url)
        elif 'POST' == method or 'PUT' == method:
            request = urllib.request.Request(url, body_bytes)
        request.get_method = lambda: method
        for key, value in options['headers'].items():
            request.add_header(key, value)
        try:
            conn = urllib.request.urlopen(request)
            return conn.read()
        except urllib.error.HTTPError as e:
            traceback.print_exc()

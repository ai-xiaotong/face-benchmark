# -*- coding:utf-8 -*-
import json

from aliyun_api import AliyunApi
from helper import b64encode_image
import traceback


class AliyunFaceApi:

    def __init__(self, ak_id, ak_key):
        self.aliyun_api = AliyunApi(ak_id, ak_key)
        self.url = 'https://dtplus-cn-shanghai.data.aliyuncs.com/face/verify'

    def verify(self, path1, path2):
        body = {
            'type': 1,
            'content_1': b64encode_image(path1).decode('utf-8'),   # image base64
            'content_2': b64encode_image(path2).decode('utf-8')    # image base64
        }
        try:
            respStr = self.aliyun_api.post(self.url, json.dumps(body).encode('utf-8'))
            resp = json.loads(respStr.decode('utf-8'))
            return resp['confidence']
        except Exception as e:
            traceback.print_exc()

# -*- coding:utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

from tencentcloud.iai.v20180301 import iai_client, models

from helper import b64encode_image
import traceback


class TencentCloudFaceApi:

    def __init__(self, ak_id, ak_secret, version='3.0'):
        cred = credential.Credential(ak_id, ak_secret)
        self.client = iai_client.IaiClient(cred, 'ap-shenzhen')
        self.version = version

    def compare(self, path1, path2):
        try:
            req = models.CompareFaceRequest()
            req.ImageA = b64encode_image(path1).decode('utf-8')
            req.ImageB = b64encode_image(path2).decode('utf-8')
            req.FaceModelVersion = self.version
            req.QualityControl = 0
            resp = self.client.CompareFace(req)
            return resp.Score
        except TencentCloudSDKException as err:
            traceback.print_exc()

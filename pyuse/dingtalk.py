#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 4:13 PM
# @Author  : Yongchin
import time
import requests
import base64
import hashlib
import hmac
import urllib.parse


class DingTalk:
    def __init__(self,
                 access_token: str = None,
                 key: str = None,
                 app_secret: str = None,
                 at_mobiles: list = None,
                 is_at_all: bool = False):
        """
         access_token:  钉钉机器人Webhook地址中的access_token
         key: 如果钉钉机器人安全设置了关键字，则需要传入对应的关键字。
         app_secret: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
         at_mobiles: 发送通知钉钉中要@人的手机号列表，如：[137xxx, 188xxx]。
         is_at_all: 是否@所有人，默认为False, 设为True则会@所有人。
        success:
                {"errcode":0, "errmsg":"ok"}
            fail:
                {"errcode":错误码, "errmsg":"失败原因"}
        """
        self.url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}"
        self.key = key
        self.app_secret = app_secret
        self.at_mobiles = at_mobiles
        self.is_at_all = is_at_all

        self.title = None

    def set_config(self, **kwargs):
        """
        set the config
        """
        if "key" in kwargs:
            self.key = kwargs["key"]
        if "app_secret" in kwargs:
            self.app_secret = kwargs["app_secret"]
        if "at_mobiles" in kwargs:
            self.at_mobiles = kwargs["at_mobiles"]
        if "is_at_all" in kwargs:
            self.is_at_all = kwargs["is_at_all"]

    def _get_stamp(self) -> dict:
        """
        https://open.dingtalk.com/document/group/enterprise-created-chatbot
        get sign method from https://open.dingtalk.com/document/robots/customize-robot-security-settings
        """
        timestamp = str(round(time.time() * 1000))
        app_secret_enc = self.app_secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.app_secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

        # sign = base64.b64encode(hmac_code).decode('utf-8')
        return {"sign": sign, "timestamp": timestamp}

    def send(self, text):
        """
        send dingtalk notice
        """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": '{}({})'.format(self.title, self.key),
                "text": text
            },
            "at": {
                "atMobiles": self.at_mobiles,
                "isAtAll": self.is_at_all
            }
        }
        params = {

        }
        if self.app_secret is not None:
            params = self._get_stamp()
        resp = requests.post(url=self.url, json=data, headers=params).json()
        if resp["errcode"] == 0:
            print(" 📧 dingTalk sent successfully!!")
        else:
            print("❌ dingTalk failed to send!!")
            print(resp)
        return resp


if __name__ == '__main__':
    # ding = DingTalk(
    #     access_token="690900b5ce6d5d10bb1218b8e64a4e2b55f96a6d116aaf50",
    #     key="xxxx",
    #     app_secret="xxxxx",
    #     at_mobiles=[13700000000, 13800000000],
    #     is_at_all=False,
    # )
    ding = DingTalk(
        access_token="4fa5c5aa96a3eb982c545e6c37d2f40e31ced8f888b25fe8d7f039753b6b28ed",
        app_secret="SEC72ec328612dce5b1f5bf3ced118cd75aa9dae66c7603913d53c7d890435efe3c",
        at_mobiles=[15025463191],
        is_at_all=False,
    )
    ding.send("#headrs")
    a = DingTalk()

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 4:13 PM
# @Author  : Yongchin
import time
import requests
import base64
import hashlib
import urllib
import hmac


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

    def set_config(self,
                   access_token: str = None,
                   key: str = None,
                   app_secret: str = None,
                   at_mobiles: list = None,
                   is_at_all: bool = False):
        """
        set the config
        :param access_token:
        :param key:
        :param app_secret:
        :param at_mobiles:
        :param is_at_all:
        :return:
        """
        self.url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}"
        self.key = key
        self.app_secret = app_secret
        self.at_mobiles = at_mobiles
        self.is_at_all = is_at_all

    def _get_stamp(self) -> dict:
        """
        Counter sign
        """
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.app_secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.app_secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
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
        resp = requests.post(url=self.url, json=data, params=params).json()
        if resp["errcode"] == 0:
            print(" 📧 dingTalk sent successfully!!")
        else:
            print("❌ dingTalk failed to send!!")
            print(resp)
        return resp


if __name__ == '__main__':
    ding = DingTalk(
        access_token="690900b5ce6d5d10bb1218b8e64a4e2b55f96a6d116aaf50",
        key="xxxx",
        app_secret="xxxxx",
        at_mobiles=[13700000000, 13800000000],
        is_at_all=False,
    )
    ding.set_config(access_token="690900b5ce6d5d10bb1218b8e64a4e2b55f96a6d116aaf50",
                    key="xxxx",
                    app_secret="xxxxx",
                    at_mobiles=[13700000000, 13800000000],
                    is_at_all=False, )
    a = DingTalk()

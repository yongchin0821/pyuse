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
                 is_at_all: bool = False,
                 title: str = None):
        """
        Args:
            access_token: 钉钉机器人Webhook地址中的access_token
            key: 如果钉钉机器人安全设置了关键字，则需要传入对应的关键字。
            app_secret: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
            at_mobiles: 发送通知钉钉中要@人的手机号列表，如：[137xxx, 188xxx]。
            is_at_all: 是否@所有人，默认为False, 设为True则会@所有人。
        """
        self.access_token = access_token
        self.URL = "https://oapi.dingtalk.com/robot/send"
        self.key = key
        self.app_secret = app_secret
        self.at_mobiles = at_mobiles
        self.is_at_all = is_at_all

        self.title = title

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
        if "access_token" in kwargs:
            self.access_token = kwargs["access_token"]
        if "title" in kwargs:
            self.title = kwargs["title"]

    def _sign(self) -> dict:
        """
        get sign method from https://open.dingtalk.com/document/robots/customize-robot-security-settings
        """
        timestamp = str(round(time.time() * 1000))
        app_secret_enc = self.app_secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.app_secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return {"sign": sign, "timestamp": timestamp}

    def send(self, text):
        """
        desc:
            send dingtalk notice
        Args:
            text:
                some text to send
        return:
            success:
                {"errcode":0, "errmsg":"ok"}
            fail:
                {"errcode":errcode, "errmsg":"errmsg"}
        """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": '{0}({1})'.format(self.title, self.key),
                "text": text
            },
            "at": {
                "atMobiles": self.at_mobiles,
                "isAtAll": self.is_at_all
            }
        }
        params = {
            "access_token": self.access_token
        }
        if self.app_secret is not None:
            params.update(self._sign())
        resp = requests.post(url=self.URL, json=data, params=params).json()
        if resp["errcode"] == 0:
            print("📧 dingTalk sent successfully!!")
        else:
            print("❌ dingTalk sent failed!!")
            print(resp)
        return resp


if __name__ == '__main__':
    ding = DingTalk(
        access_token="4fa5c5aa96x7f039753b6b28ed",
        # key="xxxx",
        app_secret="SEC016da7eex6427b305983",
        at_mobiles=[13500000000, 13800000000],
        # is_at_all=False,
    )
    ding.send("some text")
    ding.set_config(
        access_token="4faxxxxxxxxxxxxxxxxxxxxxxxxx6b28ed",
        key="xxxx",
        app_secret="SECxxxxxxxxxxxxxxx305983",
        at_mobiles=[13500000000, 13800000000],
        is_at_all=False,
    )

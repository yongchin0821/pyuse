#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 3:50 PM
# @Author  : Yongchin

import random
import string


class DatasGenerator:
    @staticmethod
    def get_phone() -> str:
        phone = random.choice(['139', '188', '185', '136', '158', '151']) + ''.join(
            random.choice("0123456789") for i in range(8))
        return phone

    @staticmethod
    def get_username(lenth: int = 6) -> str:
        admin = ''.join(random.choice(string.ascii_letters) for i in range(lenth))
        return admin

    @staticmethod
    def get_passwd(lenth: int = 8) -> str:
        passwd = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + ''.join(
            random.choice("0123456789") for i in range(lenth))
        return passwd

    @staticmethod
    def get_email(lenth: int = 6) -> str:
        email_head = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + ''.join(
            random.choice("0123456789") for i in range(lenth))
        email = email_head + random.choice(['@qq.com', '@163.com', '@gmail.com', "@yahoo.com", "@live.com"])
        return email


if __name__ == '__main__':
    g = DatasGenerator()
    print(g.get_phone())
    print(g.get_username())
    print(g.get_passwd())
    print(g.get_email())

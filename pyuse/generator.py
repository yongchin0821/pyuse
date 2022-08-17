#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 3:50 PM
# @Author  : Yongchin

import random
import string
import datetime


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

    @staticmethod
    def get_number(lenth: int = 6) -> str:
        return ''.join(random.choice("0123456789") for i in range(lenth))

    @staticmethod
    def get_IDcard():
        idcard = "500104"
        idcard = idcard + str(random.randint(1950, 2018))  # 年份项
        da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
        idcard = idcard + da.strftime('%m%d')
        idcard = idcard + str(random.randint(100, 300))  # ，顺序号简单处理

        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(idcard)):
            count = count + int(idcard[i]) * weight[i]
        idcard = idcard + checkcode[str(count % 11)]  # 算出校验码
        return idcard

    @staticmethod
    def get_plateNum():
        plateNum = random.choice(['渝A', '渝B', '渝C', '渝D', '渝E', '渝F']) + ''.join(
            random.choice(string.ascii_uppercase + "0123456789") for i in range(5))
        return plateNum

    @staticmethod
    def get_vin():
        digipercase = string.digits + string.ascii_uppercase  # 数字大写字母集合
        digiper1 = digipercase.replace('I', '')  # 去大写I
        digiper2 = digiper1.replace('O', '')  # 去大写O
        digiper3 = digiper2.replace('Q', '')  # 去大写Q
        digiper4 = digiper3.replace('Z', '')  # 去大写Z
        VIN_number = ''.join(random.choice(digiper4) for i in range(8)) + random.choice(string.digits) + random.choice(
            string.digits) + ''.join(random.choice(digiper4) for i in range(3)) + ''.join(
            random.choice(string.digits) for i in range(4))
        hs = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
              'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9,
              'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, }
        VIN = (hs[VIN_number[0]] * 8 + hs[VIN_number[1]] * 7 + hs[VIN_number[2]] * 6 + hs[VIN_number[3]] * 5 + hs[
            VIN_number[4]] * 4 + hs[VIN_number[5]] * 3 + hs[VIN_number[6]] * 2 + hs[VIN_number[7]] * 10 + hs[
                   VIN_number[9]] * 9 + hs[VIN_number[10]] * 8 + hs[VIN_number[11]] * 7 + hs[VIN_number[12]] * 6 + hs[
                   VIN_number[13]] * 5 + hs[VIN_number[14]] * 4 + hs[VIN_number[15]] * 3 + hs[VIN_number[16]] * 2) % 11
        if VIN == 10:
            VIN = 'X'
        else:
            pass
        TrueVIN = VIN_number[:8] + str(VIN) + VIN_number[9:]
        # print (str(VIN) + ':' + str(TrueVIN))
        return str(TrueVIN)


if __name__ == '__main__':
    g = DatasGenerator()
    print(g.get_phone())
    print(g.get_username())
    print(g.get_passwd())
    print(g.get_email())

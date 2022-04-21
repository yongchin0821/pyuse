#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 3:48 PM
# @Author  : Yongchin
import time
import datetime


class Time:
    def __init__(self):
        """
        Commonly used format codes:
            %y 两位数的年份表示（00-99）
            %Y 四位数的年份表示（000-9999）
            %m 月份（01-12）
            %d 月内中的一天（0-31）
            %H 24小时制小时数（0-23）
            %I 12小时制小时数（01-12）
            %M 分钟数（00=59）
            %S 秒（00-59）
            %a 本地简化星期名称
            %A 本地完整星期名称
            %b 本地简化的月份名称
            %B 本地完整的月份名称
            %c 本地相应的日期表示和时间表示
            %j 年内的一天（001-366）
            %p 本地A.M.或P.M.的等价符
            %U 一年中的星期数（00-53）星期天为星期的开始
            %w 星期（0-6），星期天为星期的开始
            %W 一年中的星期数（00-53）星期一为星期的开始
            %x 本地相应的日期表示
            %X 本地相应的时间表示
            %Z 当前时区的名称
            %% %号本身
        """
        self._time = time.ctime()
        self._struct_time = time.strptime(self._time)
        self._timestamp = time.mktime(self._struct_time)

    @property
    def time(self):
        return time.strftime("%a %b %d %H:%M:%S %Y", self._struct_time)

    @time.setter
    def time(self, value: str):
        self._time = value
        try:
            self._struct_time = time.strptime(self._time)
            return
        except Exception:
            pass
        try:
            self._struct_time = time.strptime(self._time, "%Y年%m月%d日 %H:%M:%S")
            return
        except Exception:
            pass
        try:
            self._struct_time = time.strptime(self._time, "%Y-%m-%d %H:%M:%S")
            return
        except Exception as e:
            raise ("321", repr(e))


    @property
    def timestamp(self):
        return time.mktime(self._struct_time)

    @timestamp.setter
    def timestamp(self, val):
        self._struct_time = time.localtime(val)

    @staticmethod
    def get_date():
        """
        返回年月日时分
        格式为2020-6-3 下午3:25
        :return: 返回时间
        """
        timenow = datetime.datetime.now()
        Year = timenow.strftime('%Y')
        mounth = timenow.strftime('%m')
        day = timenow.strftime('%d')

        time = timenow.strftime('%r')
        Hour = time[0:2]
        Minute = time[3:5]

        ampm = time[-2:]
        if ampm == 'AM':
            ampm = '上午'
        elif ampm == 'PM':
            ampm = '下午'
        else:
            pass

        date = "{0}-{1}-{2} {3}{4}:{5}".format(Year, str(int(mounth)), str(int(day)), ampm, str(int(Hour)), Minute)

        return date

    @staticmethod
    def to_timestamp(jikan, index):
        """
        Desc:
            时间转时间戳
            "%Y-%m-%d %H:%M:%S"
        Args:
            jikan: <list> 传入时间
            index: <list> 索引格式，例如"%Y-%m-%d %H:%M:%S"
        Example:
            to_timestamp('2020年12月21日', '%Y年%m月%d日')
        return:
            timestamp：时间戳
        """
        struct_time = time.strptime(jikan, index)
        timestamp = time.mktime(struct_time)
        return timestamp

    @staticmethod
    def to_jikan(timestamp: int, index: str):
        """
        Desc:
            timestamp to time
        Args:
            timestamp: <int> 传入时间，单位为毫秒
            index: <string> 索引格式，例如"%Y-%m-%d %H:%M:%S"
        Example:
            to_jikan('1650526296526', '%Y年%m月%d日')
        return:
            jikan：时间
        """
        jikan = time.strftime(index, time.localtime(timestamp / 1000))
        return jikan

    @staticmethod
    def time_now():
        """
        return:
            timenow: 返回年月日时分秒
            '2021-03-11 10:51:11'
        """
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return timenow

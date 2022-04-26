#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 9:55 AM
# @Author  : Yongchin


from pyuse import useTime
from pyuse import usePath

# time.strptime("2021年01月012日 12:00:00")
# t = useTime()
# print(t.time)
# print(t.timestamp)
#
# t.timestamp = 1650528033
# print(t.time)
# print(t.timestamp)
# print(t.year)
# print(t.month)

path = usePath()
print(path.path("~/jifjids/test.py"))
path._file_path="!23"




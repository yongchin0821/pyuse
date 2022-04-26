#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 8:51 AM
# @Author  : Yongchin
import sys
import os


class Path:
    def __init__(self):
        self._floder_path = None
        self._exec_path = os.getcwd()
        self._file_path = sys.path[0]
        self._filename = os.path.split(sys.argv[0])[1].split(".py")[0]
        self._alias = {"~": self._exec_path}

    @property
    def floder_path(self):
        return self._floder_path

    @property
    def exec_path(self):
        return self._exec_path

    @property
    def file_path(self):
        return self._file_path

    @property
    def filename(self):
        return self._filename

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value

    def path(self, path: str) -> str:
        for (k, v) in self._alias.items():
            path = path.replace(k, v)

        return path

    @staticmethod
    def recursive_filename(path, *args):
        """
        获取指定路径下的所有子文件
        ***该函数不会返回文件夹名字***
        :param path: 指定路径
        :param args: 文件后缀，可多传，例如.zip, .rar
        :return: 文件名列表
        """
        L = []
        if args:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if os.path.splitext(file)[1] in args:  # 想要保存的文件格式
                        L.append(os.path.join(root, file))
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    L.append(os.path.join(root, file))
        L.sort()
        return L

    @staticmethod
    def list_filename(path, *args):
        """
        获取指定路径下的所有子文件
        :param path: 指定路径
        :param args: 文件后缀，可多传，例如.zip, .rar
        :return: 文件名列表
        """
        L = os.listdir(path)
        L2 = []
        if args:
            for i in L:
                if os.path.splitext(i)[1] in args:
                    L2.append(i)
        else:
            L2 = L
        L2.sort()
        return L2


if __name__ == '__main__':
    p = Path()
    print(p.floder_path)
    print(p.exec_path)
    print(p.file_path)
    print(p.filename)
    print(p.alias)
    print(p.path("~/reports/log.txt"))

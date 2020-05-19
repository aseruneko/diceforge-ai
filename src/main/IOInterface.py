#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
入出力を行うクラスはこのクラスを継承して
readとwriteを実装すること
"""

__author__ = "yochi"
__date__ = "19 May 2020"

class IOInterface:

    """
    read():
        標準入力から文字列を受け取る

    write():
        標準出力に書き込む
    """

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


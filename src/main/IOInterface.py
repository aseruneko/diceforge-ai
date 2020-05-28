#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
入出力を行うクラスはこのクラスを継承して
readとwriteを実装すること
"""

__author__ = "yochi, aseruneko"
__date__ = "28 May 2020"

from abc import ABCMeta, abstractmethod

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


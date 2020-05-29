#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
- 標準入出力を利用するクラスが継承すべきクラス
"""

"""
- 入出力を行うクラスはこのクラスを継承してreadとwriteを実装すること
- 現状はDiceForgeにのみ実装されている
"""

__author__ = "yochi, aseruneko"
__date__ = "29 May 2020"

from abc import ABCMeta, abstractmethod

class IOInterface:

    """
    [抽象メソッド]
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


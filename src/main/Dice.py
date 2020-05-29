#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
define dice
"""

__author__ = "yochi, aseruneko"
__date__ = "28 May 2020"

import random
from main.Face import Face

class Dice:

    """
    __init__():
        ダイスの目の初期化。
        今は仮実装。
        そもそもダイスは2パターンあるからね。

    roll():
        ダイスを振ってself.topにランダムなfaceを置く。
        返り値自体もself.topになっている

    choice(num):
        num番目のfaceを返す。

    replace(num, other):
        num番目のfaceをotherと入れ替える。

    """

    def __init__(self, face_id_list):#ダイスの目を初期化。仮実装
        self.faces = []
        for face_id in face_id_list:
            self.faces.append(Face(face_id))
        self.roll()

    def roll(self):
        self.top = random.choice(self.faces)
    
    def choice(self, num):
        return self.faces[num]

    def replace(self, face, num):
        self.faces[num] = face

    def __str__(self):
        output = ""
        for i in range(6):
            output += str(self.faces[i]) + ", "
        return output
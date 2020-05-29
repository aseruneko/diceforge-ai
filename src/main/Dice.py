#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ゲームで使用するダイスのクラス
"""

"""
- Faceクラスを6つ所持する
- 基本的にはダイスを転がして、上になった面を参照する機能
"""

__author__ = "yochi, aseruneko"
__date__ = "29 May 2020"

import random
from main.Face import Face

class Dice:

    """
    [インスタンス変数]

        faces
            ダイスの持つ6つのFaceの配列

        top
            ダイスが現在向いている上の面のFace

    [インスタンスメソッド]

        __init__(face_id_list):
            face_id_list    -  作成するダイスの持つFaceのidの配列

        roll():
            ダイスを振ってself.topにランダムなfaceを置く。
            返り値自体もself.topになっている

        choice(num):
            num番目のfaceを返す。

        replace(num, other):
            num番目のfaceをotherと入れ替える。

    """

    def __init__(self, face_id_list):
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
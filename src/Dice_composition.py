#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

class Dice_composition:
    def __init__(self):#ダイスの目を初期化
        self.faces = [
            Face(),
            Face(),
            Face(),
            Face(),
            Face(),
            Face()
        ]

    def role(self):#ランダムに振って出目のfaceオブジェクトを返す
        return self.faces.choice()
    
    def choice(self, num):#num番目の出目を返す
        return self.faces[num]

    def replace(self, face, num):#与えられたfaceオブジェクトでnum番目の目を交換する
        self.face[num] = face

class Face:
    def __init__(self):#何かしら初期化

    def effect(self):#ダイスの効果を発揮する


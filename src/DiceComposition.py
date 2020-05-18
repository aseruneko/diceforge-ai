#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
define dice
"""


__author__ = "willofhare aka yochi"
__status__ = "production"
__date__ = "17 May 2020"

import random

class Dice:
    def __init__(self):#ダイスの目を初期化。仮実装
        self.faces = [
            Face("gold", 1),
            Face("vp", 1),
            Face("sun", 1),
            Face("moon", 1),
            Face("+", [["sun", 1],["moon",1]]),
            Face("?", [["gold", 1],["vp",1]])
        ]
        self.roll()

    def roll(self):#ランダムに振って出目のfaceオブジェクトを返す
        self.top = random.choice(self.faces)
    
    def choice(self, num):#num番目の出目を返す
        return self.faces[num]

    def replace(self, face, num):#与えられたfaceオブジェクトでnum番目の目を交換する
        self.face[num] = face

class Face:
    def __init__(self, tag, val):#初期化、これでいいのか思案中
        self.tag = tag
        self.val = val

    def __single_effect(self, tag, val, player):#実際に起きるエフェクト
        if tag == "gold":
            player.resource.add_gold(val)
        if tag == "vp":
            player.resource.add_victory_point(val)
        if tag == "sun":
            player.resource.add_sun(val)
        if tag == "moon":
            player.resource.add_moon(val)

    def effect(self, player):
        if self.tag in ["gold", "vp", "sun", "moon"]:
            self.__single_effect(self.tag, self.val, player)

        if self.tag == "+":
            for item in self.val:
                self.__single_effect(item[0], item[1], player)

        if self.tag == "?":
            item = random.choice(self.val)#仮実装
            self.__single_effect(item[0], item[1], player)

        if self.tag == "*3":
            of = __get_other_face()
            if of.tag in ["gold", "vp", "sun", "moon"]:
                self.__single_effect(of.tag, of.val * 3, player)
            if of.tag == "+":
                for item in of.val:
                    self.__single_effect(item[0], item[1] * 3, player)
            if of.tag == "?":
                item = random.choice(self.val)#仮実装
                self.__single_effect(item[0], item[1] * 3, player)

        if self.tag == "mirror":
            of = self.__get_other_face()
            of.effect(player)

    def __get_other_face(self):
        1==1#他のフェイスを取得して返す(何も書かないとエラーはいた)
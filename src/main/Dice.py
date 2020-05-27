#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
define dice and face
"""


__author__ = "yochi"
__date__ = "27 May 2020"

import random

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

    def roll(self):
        self.top = random.choice(self.faces)
    
    def choice(self, num):
        return self.faces[num]

    def replace(self, face, num):
        self.faces[num] = faces

class Face:

    """
        __init__(tag,val):
            Faceオブジェクトはtagとvalのペアとしている。
            tagはどんな絵柄か、valはその数を基本として表す。
            tagが?や+の場合はvalが[tag,val]の配列になる。
            鏡や*3はどうすべき?

        __single_effect(tag,val,player):
        effect(player):
        __get_other_face:
            書いたはいいけどFaceオブジェクトがPlayerのresourceに干渉するのは無理がある。
            特に、鏡は他人の出目を参照する必要があり全員の出目をfaceに送らなくちゃいけない。
            多分そのうち別のオブジェクトに機能が移されるメソッド群です。
    """

    def __init__(self, tag, val):
        self.tag = tag
        self.val = val

    def __single_effect(self, tag, val, player):
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
        pass
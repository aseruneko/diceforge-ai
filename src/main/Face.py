#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
define dice
"""

__author__ = "yochi, aseruneko"
__date__ = "28 May 2020"

import random
import os
import json

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

    name_list = []
    tag_list = []
    val_list = []
    cost_list = []

    @classmethod
    def load_face_data(cls):
        path = os.path.join(os.path.dirname(__file__), 'data/FaceData.json')
        with open(path) as f:
            j = json.load(f)
        for face in j["card_list"]:
            cls.name_list.append(face["name"])
            cls.tag_list.append(face["tag"])
            cls.val_list.append(face["val"])
            cls.cost_list.append(face["cost"])

    def __init__(self, id):
        if len(Face.name_list) == 0:
            Face.load_face_data()
        self.name = Face.name_list[id]
        self.tag = Face.tag_list[id]
        self.val = Face.val_list[id]
        self.cost = Face.cost_list[id]

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

    def __str__(self):
        output = ""
        output += self.tag + " " + str(self.val)
        return output

    def __get_other_face(self):
        pass
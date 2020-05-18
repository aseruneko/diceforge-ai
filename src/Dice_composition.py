#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

__author__ = "willofhare aka yochi"
__status__ = "production"
__date__ = "17 May 2020"


class Dices:
    def __init__(self):#ダイスを二つ持っている
        self.dice1 = Dice()
        self.dice2 = Dice()
    
    def role(self):#ダイスを振って出目を変更する
        self.dice1.roll()
        self.dice2.roll()

    def effect(self, player):#今出ている出目の効果を解決する
        self.dice1.effect()
        self.dice2.effect()


    
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

    def role(self):#ランダムに振って出目のfaceオブジェクトを返す
        self.top = self.faces.choice()
    
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
            player.resource.add_gold(self.val)
        if tag == "vp":
            player.resource.add_victory_point(self.val)
        if tag == "sun":
            player.resource.add_sun(self.val)
        if tag == "moon":
            player.resource.add_moon(self.val)

    def effect(self, player):
        if self.tag in ["gold", "vp", "sun", "moon"]:
            __single_effect(self.tag, self.val, player)

        if self.tag == "+":
            for item in self.val:
                __single_effect(item[0], item[1], player)

        if self.tag == "?":
            item = self.val.choice()#仮実装
            __single_effect(item[0], item[1], player)

        if self.tag == "*3":
            of = __get_other_face()
            if of.tag in ["gold", "vp", "sun", "moon"]:
                __single_effect(of.tag, of.val * 3, player)
            if of.tag == "+":
                for item in of.val:
                    __single_effect(item[0], item[1] * 3, player)
            if of.tag == "?":
                item = self.val.choice()#仮実装
                __single_effect(item[0], item[1] * 3, player)

        if self.tag == "mirror":
            of = __get_other_face()
            of.effect(player)

    def __get_other_face(self):
        1==1#他のフェイスを取得して返す(何も書かないとエラーはいた)
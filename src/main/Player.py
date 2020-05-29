#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ゲームのプレイヤー（NPCも含む）のクラス
"""

"""
- HumanクラスとComputerクラスに継承されている
- 人間もNPCも共通して行うだろう処理、プレイヤーとしてのとれるアクションはここに記載される
"""

__author__ = "yochi"
__date__ = "29 May 2020"

from . import Dice
from . import Resource

class Player:

    """
        ************************
        ***yochiによる記載待ち***
        ************************
    """

    def __init__(self, tag):
        self.tag = tag
        self.dices = []
        self.resource = Resource.Resource()

    # ダイスロール
    def diceroll(self):
        for dice in self.dices:
            dice.roll

    #神の祝福をもらう(faceからリソースを貰う)
    def give(self):
        for dice in self.dices:
            dice.top.effect(self)

    # カードの常在型アクション
    def card_action(self):
        1==1
    
    # 購入アクション
    def buy(self, which):
        1==1

    def print_resource(self):
        print(self.tag, "'s resource")
        print("gold: ", self.resource.gold)
        print("sun:  ", self.resource.sun)
        print("moon: ", self.resource.moon)
        print("vp:   ", self.resource.victory_point)

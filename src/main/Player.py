#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import Dice
import Resource

class Player:

    def __init__(self, tag):
        self.tag = tag
        self.dices = [Dice.Dice(), Dice.Dice()]
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

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ダイスフォージで使用するリソースのクラス
"""

"""
- gold, sun, moon, vpを管理している
- 各リソースの上限も管理している
- 最終的な効果の解決はこのクラスのメソッドに着地することが多いはず
- おそらく最も早く「完成」されたクラス
"""

__author__ = "aseruneko, yuliicppy"
__date__ = "29 May 2020"

class Resource:

    """
    [クラス変数]

        INITIAL_GOLD_MAX
        INITIAL_SUN_MAX
        INITIAL_MOON_MAX
            各リソースの初期の上限値の定義
            ここに書くべきではないかもしれない...？

    [インスタンス変数]

        gold
        sun
        moon
        victory_point
            各リソースの値

        gold_max
        sun_max
        moon_max
            各リソースの上限の値

    [インスタンスメソッド]
        
        __init__():
            各リソースの初期上限値に基づいて、リソースを保管、操作できるようにする

        add_gold(addition):
        add_sun(addition):
        add_moon(addition):
        add_victory_point(addition):
            各リソースをaddition分、上限値を加味して増加させる

        substruct_gold(substruction):
        substruct_sun(substruction):
        substruct_moon(substruction):
        substruct_victory_point(substruction):
            各リソースをsubstruction分、最低0まで低減させる

        expand_gold_max(expansion):
        expand_sun_max(expansion):
        expand_moon_max(expansion):
            クラスで扱うリソースの上限値をexpansion分、上昇させる

    """

    INITIAL_GOLD_MAX = 12
    INITIAL_SUN_MAX = 6
    INITIAL_MOON_MAX = 6

    def __init__(self):
        self.gold = 0
        self.sun = 0
        self.moon = 0
        self.victory_point = 0
        self.gold_max = Resource.INITIAL_GOLD_MAX
        self.sun_max = Resource.INITIAL_SUN_MAX
        self.moon_max = Resource.INITIAL_MOON_MAX

    def add_gold(self, addition):
        self.gold += addition
        if self.gold > self.gold_max:
            self.gold = self.gold_max
    
    def add_sun(self, addition):
        self.sun += addition
        if self.sun > self.sun_max:
            self.sun = self.sun_max

    def add_moon(self, addition):
        self.moon += addition
        if self.moon > self.moon_max:
            self.moon = self.moon_max

    def add_victory_point(self, addition):
        self.victory_point += addition

    def substract_gold(self, substraction):
        self.gold -= substraction
        if self.gold < 0:
            self.gold = 0

    def substract_sun(self, substraction):
        self.sun -= substraction
        if self.sun < 0:
            self.sun = 0

    def substract_moon(self, substraction):
        self.moon -= substraction
        if self.moon < 0:
            self.moon = 0

    def substract_victory_point(self, substraction):
        self.victory_point -= substraction
        if self.victory_point < 0:
            self.victory_point = 0

    def expand_gold_max(self, expansion):
        self.gold_max += expansion

    def expand_sun_max(self, expansion):
        self.sun_max += expansion

    def expand_moon_max(self, expansion):
        self.moon_max += expansion

    def print_all_variables(self):
        output = ""
        output += "Gold: " + str(self.gold) + ", "
        output += "Sun: " + str(self.sun) + ", "
        output += "Moon: " + str(self.moon) + ", "
        output += "VictoryPoint: " + str(self.victory_point)
        print(output)
    
# test code
if __name__ == '__main__':

    resource = Resource()
    resource.print_all_variables()

    resource.add_gold(1)
    resource.add_sun(2)
    resource.add_moon(3)
    resource.add_victory_point(4)
    resource.print_all_variables()

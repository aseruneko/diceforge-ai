#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ダイスフォージのカードのクラス
"""

"""
- カードに関しては全体的に未実装な物が多い
- ダイス（Dice.py）に関しての実装が終わったあとにそれを参考に実装していきたい
"""

__author__ = "aseruneko"
__date__ = "29 May 2020"

class Card:

    """
    [インスタンス変数]

        name
            カードの名前（ex. HAMMER）
        
        logical_name
            カードの論理名（ex. 鍛冶神のハンマー）
        
        cost_sun
        cost_moon
            カードのコスト
        
        victory_point
            カードの持つ勝利点

        instant_effect
            カードの持つ購入時効果（後でEffectクラスを実装し、代入する）

        passive_effect
            カードの持つ永続効果（後でEffectクラスを実装し、代入する）

        activation_effect
            カードの持つ起動効果（後でEffectクラスを実装し、代入する）
            もしかすると、activate_effectかもしれない（※要検討）
        
    [インスタンスメソッド]

        __init__(name, logical_name, cost_sun, cost_moon, victory_point, instant_effect, passive_effect, activation_effect):
            現状、すべての内容が渡されて生成されることになっているが、
            後々、jsonから呼び出して作れるようにするべき。よって、本来渡されるべきはidのみ

        __print_all_variables():
            インスタンスの持つ全ての変数を表示するデバック用メソッド。

    """

    def __init__(self, name="", logical_name="", cost_sun=0, cost_moon=0, victory_point=0, instant_effect=None, passive_effect=None, activation_effect=None):
        self.name = name
        self.logical_name = logical_name
        self.cost_sun = cost_sun
        self.cost_moon = cost_moon
        self.victory_point = victory_point
        self.instant_effect = instant_effect
        self.passive_effect = passive_effect
        self.activation_effect = activation_effect

    def __print_all_variables(self):
        output = ""
        output += "name: " + self.name + "\n"
        output += "logical_name: " + self.logical_name + "\n"
        output += "sun: " + str(self.cost_sun) + ", moon: " + str(self.cost_moon) + "\n"
        output += "victory_point: " + str(self.victory_point) + "\n"
        output += "instant_effect: " + str(self.instant_effect) + "\n"
        output += "passive_effect: " + str(self.passive_effect) + "\n"
        output += "activation_effect: " + str(self.activation_effect) + "\n"
        print(output)

    def __str__(self):
        return self.logical_name

# test code
if __name__ == '__main__':
    card = Card()
    card.__print_all_variables()

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

import os, json

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
    name_list = []
    logical_name_list = []
    cost_sun_list = []
    cost_moon_list = []
    victory_point_list = []
    instant_effect_list = []
    passive_effect_list = []
    activation_effect_list = []
    description_list = []

    @classmethod
    def load_card_data(cls):
        # jsonを読む
        path = os.path.join(os.path.dirname(__file__), 'data/CardData.json')
        with open(path,encoding="utf-8_sig") as f:
            j = json.load(f)
        # 読んだjsonの内容をクラス変数に格納する
        # 通し番号であるidでアクセスするよう設計されている
        for card in j["card_list"]:
            cls.name_list.append(card["name"])
            cls.logical_name_list.append(card["logical_name"])
            cls.cost_sun_list.append(card["cost_sun"])
            cls.cost_moon_list.append(card["cost_moon"])
            cls.victory_point_list.append(card["victory_point"])
            cls.instant_effect_list.append(card["instant_effect"])
            cls.passive_effect_list.append(card["passive_effect"])
            cls.activation_effect_list.append(card["activation_effect"])
            cls.description_list.append(card["description"])

    def __init__(self, id):
        # 初回はjsonの読み出し処理を実行
        if len(Card.name_list) == 0:
            Card.load_card_data()
        # idに応じた値を引っ張り出してくる
        self.name = Card.name_list[id]
        self.logical_name = Card.logical_name_list[id]
        self.cost_sun = Card.cost_sun_list[id]
        self.cost_moon = Card.cost_moon_list[id]
        self.victory_point = Card.victory_point_list[id]
        self.instant_effect = Card.instant_effect_list[id]
        self.passive_effect = Card.passive_effect_list[id]
        self.activation_effect = Card.activation_effect_list[id]
        self.description = Card.description_list[id]

    def print_all_variables(self):
        output = ""
        output += "name: " + self.name + "\n"
        output += "logical_name: " + self.logical_name + "\n"
        output += "sun: " + str(self.cost_sun) + ", moon: " + str(self.cost_moon) + "\n"
        output += "victory_point: " + str(self.victory_point) + "\n"
        output += "instant_effect: " + str(self.instant_effect) + "\n"
        output += "passive_effect: " + str(self.passive_effect) + "\n"
        output += "activation_effect: " + str(self.activation_effect) + "\n"
        output += "description: " + str(self.description) + "\n"
        print(output)

    def __str__(self):
        return self.logical_name

# test code
if __name__ == '__main__':
    card = Card(0)
    card.print_all_variables()

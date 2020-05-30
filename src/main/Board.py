#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ゲームで使用するボードのクラス
"""

"""
- 現状呼び出されていない（そのためエラー有り）が、DiceForge.pyで呼び出し予定
- ゲームでボードに並べられている鍛造可能なフェイスの一覧と残数を持つのはここ
- ゲームでボードに並べられている購入可能なカードの一覧と残数を持つのもここ
- ゲームで購入ボードのどこにプレイヤーコマがいるかの情報を持つのもここ
"""

__author__ = "SYHNE, aseruneko"
__date__ = "28 May 2020"

from main.Dice import Dice
from main.Face import Face
from main.IOInterface import IOInterface
class Board(IOInterface):

    """
    [インスタンス変数]

        face_distribution
            ゲームボードの上に残っている鍛造可能なフェイスの一覧。
            Faceのリストになるだろうが、未実装

        card_distribution
            ゲームボードの上に残っている購入可能なカードの一覧。
            Cardのリストになるだろうが、未実装

    [インスタンスメソッド]

        __init__(face_distribution, card_distribution):
            face_distribution   -   ゲームボードに並べられるフェイスのidの列
            card_distribution   -   ゲームボードに並べられるカードのidの列

        reset():
            未実装

    """

    def __init__(self, face_distribution ,card_distribution ):
        self.face_distribution = face_distribution
        self.card_distribution = card_distribution

    

    def show_playable_dice_face(self):
        output =""
        for playable_dice_num, playable_face in enumerate(self.face_distribution):
            output += str(playable_dice_num) + ": " + str(Face(playable_face)) +"\n"
        self.write(output)   
        
    #def show_playable_cards(self):
    #    output= []
    #    for playable_card_num, playable_card in enumerate(self.card_distribution):
    #        output += playable_card_num + str(Card[(playable_card)]) +"\n"
    #   self.write(output)  

    def read(self):
        return input("\n> command?\n")

    def write(self, string):
        print("")
        print(string)
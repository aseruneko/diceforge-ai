#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
プレイヤーのうち、人間が操作するクラス
"""

"""
- Playerクラスを継承している
- 全体的に未実装
"""

__author__ = "aseruneko"
__date__ = "29 May 2020"

from main.Player import Player

class Human(Player):

    """
    [インスタンスメソッド]
        
        action(board, resorce, cards):
            作った気はするが実際どういう実装にするべきか忘れ去られた可愛そうなメソッド。
            今の所、どこにも使用されていない。
    """
    
    # プレイヤーの手番の処理を行う関数
    def action(self, board, resorce, cards):
        pass
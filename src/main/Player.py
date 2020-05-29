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
    [インスタンス変数]

        id
            人間あるいはコンピュータのid。
            現状は整数値。
            人間とコンピュータで重複する。

        dices
            プレイヤーが持つDiceの配列
            長さが2になるように運用してください。
            長さを固定する方法をご存じの方は書き直してね。

        resource
            プレイヤーが持つResource
    [インスタンスメソッド]
        diceroll
            dices.topをランダムに変更する。
            つまり自身のダイスを振る。

        receive_divine_blessing
            大規模変更予定。
            自身のダイスの出目の神の祝福を受け取る。
            これは他のクラスに機能が移されるでしょう。

        card_action
        buy
            未実装。
            体裁のために存在してますが、使用されているので一先ず消さないでください。
            このメソッドにおいてプレイヤーは、
            どのカードの効果を行うか、あるいは何を買うかの選択を行うに留め、
            実際の処理は別のクラスが行うようにするといいのではないかと思う。
    """

    def __init__(self, id):
        self.id = id
        self.dices = []
        self.resource = Resource.Resource()

    def diceroll(self):
        for dice in self.dices:
            dice.roll

    def receive_divine_blessings(self):
        for dice in self.dices:
            dice.top.effect(self)

    def card_action(self):
        pass
    
    def buy(self, which):
        pass

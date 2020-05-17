#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# AIは現在のラウンド数、プレイヤーとAIのリソース、ダイスの組成、ボードの状態を参照して何らかの手を出力する？

class DiceForge:

    # ゲームの実際の流れを実装
    def play(self):
        board = Board()
        player1 = computer = Computer()
        player2 = user = User()

        round = 0 
        # 以下ターンが交互に回ってきてラウンドが経過していく処理をDiceForge内に実装したい

　　# リソース(カード含める？)を参照して試合結果を表示する　
    def show_result(self, Resorce):


class dice_composition:

class Board:
    # 最初の盤面を定義する
    def __init__(self):

    def playable_dice_face()

    def playable_cards()




class Resorce:


class Card:

class Player:

    def __init__(self, resorce, cards):

    # ダイスロール
    def dicerole(self, dice_composition):
    
    # カードの常在型アクション
    def card_action(self, cards):
    
    # 購入アクション
    def buy(self, resorce, board):

    
     
class User(Player):
    
    # プレイヤーの手番の処理を行う関数
    def action(self, board, resorce, cards):


class Computer(Player):






if __name__ = '__main__':
    DiceForge().play()

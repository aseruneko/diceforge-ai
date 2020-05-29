#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ダイスフォージのゲーム本体のクラス
"""

"""
- 対話式のコマンドで操作を行うのが主機能
- 基本的に持っている情報はround数とPlayer(Human or Computer)の配列と、Boardクラス1つ
- 最も混沌としているので将来的には切り出しが必要かもしれない
"""

__author__ = "c3341, aseruneko"
__date__ = "29 May 2020"

# import Board
from . import Player
from main.Human import Human
from main.Computer import Computer
from main.IOInterface import IOInterface
from main.Dice import Dice

class DiceForge(IOInterface):

    """
    [インスタンス変数]

        player_num
            プレイヤーの人数（人間とコンピュータの総計）

        round
            ラウンド数

        face_distribution
            ゲームでボードに並べる鍛造可能なダイスフェイスのidの配列
            Boardが実装されれば、その内容はそちらが持つはずなので不要？

        card_distribution
            ゲームでボードに並べる購入可能なカードのidの配列
            Boardが実装されれば、その内容はそちらが持つはずなので不要？

        board（未実装）
            ゲームで使用するボードのデータ

        player_list
            ゲームに参加しているPlayerのリスト。
            ComputerクラスのインスタンスとHumanクラスのインスタンス、両方入る可能性がある。

    [インスタンスメソッド]
        
        __init__(player_distribution, face_distribution_type, card_distribution_type, initial_dice_face_type):
            player_distribution     -   "human"か"computer"の文字列配列
            face_distribution_type  -   ゲームで使用するフェイスの組成タイプ、詳細はmain.py
            card_distribution_type  -   ゲームで使用するカードの組成タイプ、詳細はmain.py
            initial_dice_face_type  -   ゲームで使用する初期ダイスの組成タイプ、詳細はmain.py

        game():
            ゲームのメイン処理が書かれるメソッド。
            main.pyでDiceForgeインスタンスが作成されたあと、このメソッドが呼び出される。

        read():
            コマンドを要求するメッセージを表示し、入力コマンドを返すメソッド。

        write(string):
            改行をいれたあと、stirngを出力するメソッド。
            各所でprintをするとログが取りづらいので、ゲームからの出力は一旦ここを介するように。

        write_wrong_command_message():
            無効なコマンド（illegalな操作ではない）を入力したときに呼び出されるメソッド。
            エラーログを表示する。

        choose_first_action(player):
            1つ目の行動のコマンドの入力を受け付け処理するメソッド。

        print_help():
            可能なコマンド一覧を表示するメソッド。

        make_face_distribution(face_distribution_type):
            フェイスの組成タイプを受け取り、人数を加味して、実際に使用すべきフェイスのidの配列を返すメソッド。

        make_initial_dice_face(player_list, initial_dice_face_type):
            最初のダイスの組成タイプを受け取り、各プレイヤーに対して最初のダイスを発行するコマンド。
            Playerの内部のDicesにアクセスしてDiceを追加する。
    """

    def __init__(self, player_distribution=["human","computer"], face_distribution_type="default", card_distribution_type="default", initial_dice_face_type="default"):
        self.player_num = len(player_distribution)
        self.round = 0
        self.face_distribution = self.make_face_distribution(face_distribution_type)
        self.card_distribution = [0] #仮実装
        # self.board = Board(face_distribution, card_distribution)
        self.player_list = []
        for i in range(self.player_num): # distributionに基づくPlayerの作成
            if player_distribution[i] == "human":
                self.player_list.append(Human(i))
            if player_distribution[i] == "computer":
                self.player_list.append(Computer(i))
        # typeに基づく初期ダイスの生成
        self.make_initial_face_dice(self.player_list, initial_dice_face_type)

    def game(self):
        while(self.round < 2):
            self.write("round" + str(self.round))
            for active_player in self.player_list:
                self.write(str(active_player.tag) + "'s turn")

                #全員がダイスを振るって神の祝福を受け取る
                for player in self.player_list:
                    player.diceroll()
                    player.give()
                    player.print_resource()

                #手番プレイヤーはカードの効果を解決する
                active_player.card_action()

                #faceの購入かカードの購入を選ぶ
                self.choose_first_action(active_player)

                #追加アクションを行うか選ぶ
                1==1
            self.round += 1
        self.write("game set")

    def read(self):
        return input("\n> command?\n")

    def write(self, string):
        print("")
        print(string)

    def write_wrong_command_message(self):
        self.write("> wrong command.")

    def choose_first_action(self, player):
        while(True):
            if type(player) == Human:
                self.write("face or card?")
                command = self.read()
                if command == "face":
                    player.buy("face")
                    break
                elif command == "card":
                    player.buy("card")
                    break
                elif command == "player id":
                    self.write("your player id is " + str(player.tag))
                elif command == "player dice":
                    self.write(str(player.dices[0]))
                    self.write(str(player.dices[1]))
                elif command == "help":
                    self.print_help()
                else:
                    self.write_wrong_command_message()
            else:
                break

    def print_help(self):
        output = "\n"
        output += "face\t\t-\tbuy face\n"
        output += "card\t\t-\tbuy card\n"
        output += "player id\t-\tshow player id\n"
        output += "player dice\t-\tshow player dice"
        self.write(output)

    def make_face_distribution(self, face_distribution_type):
        output = [0]
        if face_distribution_type == "default":
            if self.player_num == 2:
                pass
            if self.player_num == 3:
                pass
            if self.player_num == 4:
                pass
        if face_distribution_type == "debug":
            output = [0,0,0,0,0,0,0,0]
        return output

    def make_initial_face_dice(self, player_list, initial_dice_face_type):
        if initial_dice_face_type == "default":
            pass
        elif initial_dice_face_type == "debug":
            for player in player_list:
                player.dices.append(Dice([0,0,0,0,0,0]))
                player.dices.append(Dice([0,0,0,0,0,0]))
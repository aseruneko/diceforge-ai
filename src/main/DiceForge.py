#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Class of DiceForge (main part of game)
"""

__author__ = "c3341, aseruneko"
__status__ = "production"
__date__ = "28 May 2020"

# import Board
from . import Player
from main.User import User
from main.Computer import Computer

class DiceForge:

    def __init__(self, player_distribution=["human","computer"], face_distribution=[0], card_distribution=[0]):
        self.player_num = len(player_distribution)
        self.round = 0
        self.face_distribution = face_distribution
        self.card_distribution = card_distribution
        # self.board = Board(face_distribution, card_distribution)
        self.player_list = []
        for i in range(self.player_num):
            if player_distribution[i] == "human":
                self.player_list.append(User(i))
            if player_distribution[i] == "computer":
                self.player_list.append(Computer(i))

    def show_result(self):
        print("> show result...")

    def print_all_variables(self):
        output = ""
        output += "Number of Player: " + str(self.player_num) + "\n"
        output += "Round: " + str(self.round) + "\n"
        output += "Face Distribution: " + str(self.face_distribution) + "\n"
        output += "Card Distribution: " + str(self.card_distribution) + "\n"
        print(output)

    def game(self):
        while(self.round < 2):
            print(self.round, "round")
            for active_player in self.player_list:
                print(active_player.tag, "'s turn")

                #全員がダイスを振るって神の祝福を受け取る
                for player in self.player_list:
                    player.diceroll()
                    player.give()
                    player.print_resource()

                #手番プレイヤーはカードの効果を解決する
                active_player.card_action()

                #faceの購入かカードの購入を選ぶ
                while(True):
                    if active_player.tag == 0:
                        print("face or card?")
                        command = input()
                        if command == "face":
                            active_player.buy("face")
                            break
                        if command == "card":
                            active_player.buy("card")
                            break
                    else:
                        break

                #追加アクションを行うか選ぶ
                1==1
            self.round += 1
        print("game set")


# test code
if __name__ == '__main__':
    dice_forge = DiceForge()
    dice_forge.print_all_variables()
    dice_forge.game()

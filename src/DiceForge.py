#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Class of DiceForge (main part of game)
"""

__author__ = "c3341, aseruneko"
__status__ = "production"
__date__ = "18 May 2020"

# import Board
# import Player

class DiceForge:

    def __init__(self, player_distribution=["human","computer"], face_distribution=[0], card_distribution=[0]):
        self.player_num = len(player_distribution)
        self.round = 0
        self.face_distribution = face_distribution
        self.card_distribution = card_distribution
        # self.board = Board(face_distribution, card_distribution)
        self.player_list = []
        # for i in range(self.player_num):
        #     if player_distribution[i] == "human":
        #         self.player_list.append(Player(0))
        #     if player_distribution[i] == "computer":
        #         self.player_list.append(Player(1))

    def show_result(self):
        print("> show result...")

    def print_all_variables(self):
        output = ""
        output += "Number of Player: " + str(self.player_num) + "\n"
        output += "Round: " + str(self.round) + "\n"
        output += "Face Distribution: " + str(self.face_distribution) + "\n"
        output += "Card Distribution: " + str(self.card_distribution) + "\n"
        print(output)

# test code
if __name__ == '__main__':
    dice_forge = DiceForge()
    dice_forge.print_all_variables()

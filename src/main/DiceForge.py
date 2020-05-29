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
from main.Human import Human
from main.Computer import Computer
from main.IOInterface import IOInterface
from main.Dice import Dice

class DiceForge(IOInterface):

    def __init__(self, player_distribution=["human","computer"], face_distribution_type="default", card_distribution_type="default", initial_dice_face_type="default"):
        self.player_num = len(player_distribution)
        self.round = 0
        self.face_distribution = self.make_face_distribution(face_distribution_type)
        self.card_distribution = [0]
        # self.board = Board(face_distribution, card_distribution)
        self.player_list = []
        for i in range(self.player_num):
            if player_distribution[i] == "human":
                self.player_list.append(Human(i))
            if player_distribution[i] == "computer":
                self.player_list.append(Computer(i))
        self.make_initial_face_dice(self.player_list, initial_dice_face_type)

    def show_result(self):
        self.write("> show result...")

    def print_all_variables(self):
        output = ""
        output += "Number of Player: " + str(self.player_num) + "\n"
        output += "Round: " + str(self.round) + "\n"
        output += "Face Distribution: " + str(self.face_distribution) + "\n"
        output += "Card Distribution: " + str(self.card_distribution) + "\n"
        self.write(output)

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

    def write_wrong_message(self):
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
                    self.write_wrong_message()
            else:
                break

    def print_help(self):
        output = "\n"
        output += "face\t\t-\tbuy face\n"
        output += "card\t\t-\tbuy card\n"
        output += "player id\t-\tshow player id"
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



# test code
if __name__ == '__main__':
    dice_forge = DiceForge()
    dice_forge.print_all_variables()
    dice_forge.game()

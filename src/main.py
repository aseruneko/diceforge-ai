#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Main class of diceforge-ai
Please execute this file.
"""

__author__ = "aseruneko"
__version__ = "0.0.1a"
__status__ = "production"
__date__ = "18 May 2020"

import DiceForge

exit_flag = False

def main():
    print_title()
    while(not exit_flag):
        print("\n> command?"),
        command = input()
        command_perse(command)

def print_title():
    output = "\n"
    output += "******************************\n"
    output += "* diceforge-ai ver 0.0.1a\n"
    output += "******************************\n\n"
    output += "tips: help command provides index of command"
    print(output)

def command_perse(command):
    if command == "exit":
        global exit_flag 
        exit_flag = True
    if command == "help":
        print_help()
    if command == "start":
        print("> game starts...")
        dice_forge = DiceForge.DiceForge()
        dice_forge.game()

def print_help():
    output = "\n"
    output += "help\t-\tshow help\n"
    output += "exit\t-\texit program\n"
    output += "start\t-\tstart game"
    print(output)

if __name__ == '__main__':
    main()
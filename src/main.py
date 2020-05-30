#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
diceforge-aiのメインクラス
"""

"""
- これを実行することでプログラムが走るようにする
- 基本的に対話式のコマンドでゲームの処理を行う
"""

__author__ = "aseruneko"
__version__ = "0.0.1a"
__date__ = "29 May 2020"


from main import DiceForge

"""
[グローバル変数]

    player_distribution
        起動するゲームのプレイヤーの組成。"human"と"computer"の配列

    face_distribution_type
        起動するゲームの購入ダイスの組成のタイプ。可能な値は以下の通り。
        個々のタイプそれぞれ何人かに応じた処理はDiceForge.pyで具体的に記されている。
            "default"   -   デフォルトの組成を使用する（未実装）
            "debug"     -   デバッグ用の組成を使用する（未実装）

    card_distribution_type
        起動するゲームの購入可能カードの組成のタイプ。可能な値は以下の通り。
        個々のタイプそれぞれ何人かに応じた処理はDiceForge.pyで具体的に記されている。
            "defult"    -   デフォルトの組成を使用する（未実装）
            "debug"     -   デバッグ用の組成を使用する（未実装）
            "expert"    -   上級ルール用の組成を使用する（未実装）

    initial_dice_face_type
        起動するゲームの初期ダイスの組成のタイプ。可能な値は以下の通り。
        本来であれば固定だが、開発用にデバッグ用の開始ダイスを定義するために作成。
        個々のタイプそれぞれ何人かに応じた処理はDiceForge.pyで具体的に記されている。
            "default"   -   デフォルトの組成を使用する（未実装）
            "debug"     -   デバッグ用の組成を使用する

    round_max
        起動するゲームのラウンド数。0にすると人数に応じたデフォルト値を使用する。

    __exit_flag
        ゲームが起動していない状態でのプログラムに対してのコマンド受付を終了するためのフラグ。

[関数]

    main():
        プログラムを実行してはじめに実行される関数。
        タイトルの表示と、コマンドの受付を行う。

    command_perse(command):
        ゲームが起動していない状態でのプログラムに対するコマンドを受け取り、
        それに応じた処理を行う関数。

    print_title():
        プログラムのタイトルを表示する関数。

    print_help():
        ゲームが起動していない状態でのプログラムに対して可能なコマンド一覧を表示する関数。

[コマンド]

    help    - show help
    start   - start game
    exit    - exit program

"""

player_distribution = ["human","human"]
face_distribution_type = "default"
card_distribution_type = "default"
initial_dice_face_type = "debug"
round_max = 2

__exit_flag = False

def main():
    print_title()
    while(not __exit_flag):
        print("\n> command?"),
        command = input()
        command_perse(command)

def command_perse(command):
    if command == "exit":
        global __exit_flag 
        __exit_flag = True
    if command == "help":
        print_help()
    if command == "start":
        print("> game starts...")
        dice_forge = DiceForge.DiceForge(player_distribution, face_distribution_type, card_distribution_type, initial_dice_face_type, round_max)
        dice_forge.game()

def print_title():
    output = "\n"
    output += "******************************\n"
    output += "* diceforge-ai ver 0.0.1a\n"
    output += "******************************\n\n"
    output += "tips: help command provides index of command"
    print(output)

def print_help():
    output = "\n"
    output += "help\t\t-\tshow help\n"
    output += "start\t\t-\tstart game\n"
    output += "exit\t\t-\texit program\n"
    print(output)

if __name__ == '__main__':
    main()

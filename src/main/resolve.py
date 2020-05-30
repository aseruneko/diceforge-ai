#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
効果解決用のモジュール
"""

"""
- 後で書く
"""

__author__ = "seruneko"
__date__ = "30 May 2020"


from main.Board import Board
from main.Face import Face

"""
[関数]
    resolve_effect(player, effect):
        何らかのエフェクトを処理するメソッド。
        将来的にどこかに切り出したい。

    resolve_face(player, face):
        一つのフェイズを処理するメソッド。
        将来的にどこかに切り出したい。
"""

def resolve_effect(board, player, effect):
    print("> [Player {0}] causes effect [{1}]".format(player.id, effect)) # 開発用のログ
    if effect == "roll_2_dices":
        for dice in player.dices:
            dice.roll()
            print("> dice top is {0}".format(dice.top.name))
    elif effect == "resolve_2_dices":
        for dice in player.dices:
            resolve_face(player, dice.top)
    elif effect == "buy_face":
        board.show_playable_dice_face()
        chosen_face_number = int(input("choose number+\n"))
        chosen_face_id = board.face_distribution.pop(chosen_face_number)
        all_faces_list = []
        all_faces_list.extend(player.dices[0].faces)
        all_faces_list.extend(player.dices[1].faces)
        for face_index_number , face_number in enumerate(all_faces_list):
            print("{0}: {1}".format(face_index_number,str(face_number)))
        chosen_replace_number = int(input("choose number"+"\n"))
        if chosen_replace_number > 5 :
            player.dices[1].replace(Face(chosen_face_id),chosen_replace_number-6)
        else:
            player.dices[0].replace(Face(chosen_face_id),chosen_replace_number)



def resolve_face(player, face):
    if face.tag in ["gold", "sun", "moon", "vp"]:
        player.resource.add(face.tag, face.val)
        print("> Player {0} yields {1} {2}".format(player.id, face.val, face.tag))
    elif face.tag == "+":
        for ef in face.val:
            player.resource.add(ef["tag"], ef["val"])
            print("> Player {0} yields {1} {2}".format(player.id, ef["val"], ef["tag"]))
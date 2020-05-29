#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
使用するフェイスのデータ（json処理に完全移植完了後、削除予定）
"""

import Dice
import random

__author__ = "SYHNE"
__date__ = "19 May 2020"

Face_list = [Dice.Face("gold", 1),Dice.Face("vp", 2),
             Dice.Face("moon", 1),Dice.Face("gold", 3),
             Dice.Face("sun", 1),Dice.Face("gold", 4),
             Dice.Face("gold", 6),Dice.Face("+", [["sun", 1],["vp",1]]),Dice.Face("+", [["gold", 2],["moon",1]]),Dice.Face("?", [["sun", 1],["moon",1],["gold",1]]),
             Dice.Face("?", [["gold", 2],["vp",2]]),
             Dice.Face("moon", 2),
             Dice.Face("sun", 2),Dice.Face("vp", 3),
             Dice.Face("vp", 4),Dice.Face("+", [["vp", 2],["moon",2]]),Dice.Face("+", [["sun", 1],["moon",1],["gold",1],["vp",1]]),Dice.Face("?", [["sun", 2],["moon",2],["gold",2]])]  #= range(18)
             #現状+と?は2つにしか対応していないのに注意
Face_cost_list = [0,0,2,2,3,3,4,4,4,4,5,6,8,8,12,12,12,12]  #costは別で管理してBoard作成時に参照?
Face_amount_default = [0,0,4,4,4,4,1,1,1,1,4,4,4,4,1,1,1,1]
Face_amount_ForTwoPlayer = [0,0,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1]
face_remover = random.sample([0,0,1,1], 4)
for i in range(4):
    Face_amount_ForTwoPlayer[6+i] -=  face_remover[i]
face_remover = random.sample([0,0,1,1], 4)
for i in range(4):
    Face_amount_ForTwoPlayer[14+i] -=  face_remover[i]

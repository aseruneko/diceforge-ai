#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from data.CardSet import *
from data.FaceSet import *

__author__ = "SYHNE, aseruneko"
__date__ = "28 May 2020"

class Board:
    def __init__(self, face_distribution = None, card_distribution = None):
        #Distributionで管理 or Boardのremainで管理(playerが各々保持)?
        self.remain_faces = face_distribution
        self.remain_cards = card_distribution
        self.used_CardType = Used_CardType

    def reset(self):
        self.remain_cards = [2] * 15 #後でプレイヤー数に　
        self.remain_faces = Face_amount_ForTwoPlayer #Facesから

    #def playable_dice_face()

    #def playable_cards()
#test
if __name__ == '__main__':
    board = Board(Card_Types)
    print(board.remain_faces) # ex.[0, 0, 2, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 2, 1, 1, 0, 0]
    print(board.remain_cards) # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    print(board.used_CardType ) # [['HAMMER', 0, 1, 0], ['CHEST', 0, 1, 2], ['HIND', 0, 2, 2], ['SATYRS', 0, 3, 6], ['FERRYMAN', 0, 4, 12], ['HELMET', 0, 5, 4], ['CANCER', 0, 6, 8], ['ELDER', 1, 0, 0], ['SPIRIT', 1, 0, 2], ['OWL', 2, 0, 4], ['MINO', 3, 0, 8], ['GORGON', 4, 0, 14], ['MIRROR', 5, 0, 10], ['SPHINX', 6, 0, 10], ['HYDRA', 5, 5, 26]]

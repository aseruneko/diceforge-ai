#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import Card
from Cards import *
from Faces import *
__author__ = "SYHNE"
__status__ = "production"
__date__ = "19 May 2020"


remain_faces = []
remain_cards = []
class Board:
    def __init__(self,Used_CardType , remain_cards = None, remain_faces = None, Manual=None  ):
        #Distributionで管理 or Boardのremainで管理(playerが各々保持)?
        self.remain_cards = remain_cards
        self.remain_faces = remain_faces
        self.used_CardType = Used_CardType
        if Manual is None:
            self.reset()
        #else:
        #    self.set_Manual(Manual)
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

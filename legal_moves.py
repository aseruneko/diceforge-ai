#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "SYHNE"
__date__ = "18 May 2020"
#[name,sun_cost,moon_cost]
Standard_Card_Types = [["HAMMER",0,1],["CHEST",0,1],["HIND",0,2],["SATYRS",0,3],
                      ["FERRYMAN",0,4],["HELMET",0,5],["CANCER",0,6],["ELDER",1,0],
                      ["SPIRIT",1,0],["OWL",2,0],["MINO",3,0],["GORGON",4,0],
                      ["MIRROR",5,0],["SPHINX",6,0],["HYDRA",5,5]]  #range(15)
def pay_pattern(gold): #playerクラスに突っ込む？
    #購入が3つに収まるやつの列挙
    face_gold = [12,8,6,5,4,3,2]
    pattern = []
    #1
    for i in range(7):
        if gold >= face_gold[i]:
            pattern.append([face_gold[i]])
    #2
    for i in range(7):
        P = gold
        if P >= face_gold[i]:
            P -= face_gold[i]
            for j in range(i,7):
                if P >= face_gold[j]:
                    pattern.append([face_gold[i],face_gold[j]])
                else:
                    continue
        else:
            continue
    #3
    for i in range(7):
        P = gold
        if P >= face_gold[i]:
            Q = P - face_gold[i]
            for j in range(i,7):
                if Q >= face_gold[j]:
                    R = Q - face_gold[j]
                    for k in range(j,7):
                        if R >= face_gold[k]:
                            pattern.append([face_gold[i],face_gold[j],face_gold[k]])
                        else:
                            continue
                else:
                    continue
        else:
            continue
    return pattern


def legal_moves(resource): #resorce = [金、太陽、月]
    l_move = {}
    l_move["gold"] = pay_pattern(resource[0])
    l_move["card"] = []
    for card in Standard_Card_Types:
        if resource[1] >= card[1] and resource[2] >= card[2]:
            l_move["card"].append(card)
    return l_move
resource = [6,4,3]
print(legal_moves(resource))
# {'gold': [[6], [5], [4], [3], [2], [4, 2], [3, 3], [3, 2], [2, 2], [2, 2, 2]], 'card': [['HAMMER', 0, 1], ['CHEST', 0, 1], ['HIND', 0, 2], ['SATYRS', 0, 3], ['ELDER', 1, 0], ['SPIRIT', 1, 0], ['OWL', 2, 0], ['MINO', 3, 0], ['GORGON', 4, 0]]}

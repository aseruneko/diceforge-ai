#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "SYHNE"
__status__ = "production"
__date__ = "19 May 2020"
#[name,cost_sun,cost_moon_victory_point]
gametype = 0
if gametype == 0:
    Card_Types = [["HAMMER",0,1,0],["CHEST",0,1,2],["HIND",0,2,2],["SATYRS",0,3,6],
                  ["FERRYMAN",0,4,12],["HELMET",0,5,4],["CANCER",0,6,8],["ELDER",1,0,0],
                  ["SPIRIT",1,0,2],["OWL",2,0,4],["MINO",3,0,8],["GORGON",4,0,14],
                  ["MIRROR",5,0,10],["SPHINX",6,0,10],["HYDRA",5,5,26]]  #range(15) #logical_name と各effectの有無などもつける

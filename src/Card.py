#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
definition of Card
"""

__author__ = "aseruneko"
__status__ = "production"
__date__ = "17 May 2020"

class Card:
    
    def __init__(self, name="", logical_name="", cost_sun=0, cost_moon=0, victory_point=0, instant_effect=None, passive_effect=None, activation_effect=None):
        self.name = name
        self.logical_name = logical_name
        self.cost_sun = cost_sun
        self.cost_moon = cost_moon
        self.victory_point = victory_point
        self.instant_effect = instant_effect
        self.passive_effect = passive_effect
        self.activation_effect = activation_effect

    def print_all_variables(self):
        output = ""
        output += "name: " + self.name + "\n"
        output += "logical_name: " + self.logical_name + "\n"
        output += "sun: " + str(self.cost_sun) + ", moon: " + str(self.cost_moon) + "\n"
        output += "victory_point: " + str(self.victory_point) + "\n"
        output += "instant_effect: " + str(self.instant_effect) + "\n"
        output += "passive_effect: " + str(self.passive_effect) + "\n"
        output += "activation_effect: " + str(self.activation_effect) + "\n"
        print(output)

# test code
if __name__ == '__main__':
    card = Card()
    card.print_all_variables()
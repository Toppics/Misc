# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:17:07 2021

@author: yan-s
"""

def yes_no(answer):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
     
    while True:
        choice = input(answer).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
           print("Please respond with 'yes' or 'no'\n")
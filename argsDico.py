# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:49:30 2022

@author: yan-s
"""

def setVar(a, b, c, d):
    x0 = a
    x1 = b
    x2 = c
    x3 = d
    
    print(x0, x1, x2, x3)
      
argsDico = {'a': True, 'b': 290.1, 'c': 'Yes', 'd': False}

setVar(**argsDico)

Dico = {
        'listyUp': [], 
        'upperLonCorrection': -0.0005, 'upperLatCorrection': 0.001, 'upperColor': 'red',
        'upwardLonCorrection': -0.01, 'upwardLatCorrection': 0.001, 'upwardColor': 'black',
        'downwardLonCorrection': -0.013, 'downwardLatCorrection': -0.004, 'downwardColor': 'black',
        'normalLonCorrection': 0, 'normalLatCorrection': 0.001, 'normalColor': 'black',
        'arrowColor': 'blue'
        }
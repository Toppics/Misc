# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:42:55 2022

@author: yan-s
"""

a = (('GA','be'), ('dx', 'xd'))
b = (('rf', 'gh'), ('ty', 'hu'))
c = ['a', 'b', 'g']

for x in zip(a,b):
    print(x)
    
def func(x):
    return x.upper()

for x in map(func, c):
    print(x)
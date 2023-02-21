# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:17:55 2022

@author: yan-s
"""


def compare(a, b):
    if a == b:
        return a, b


mylist = ['1', 1, 4, ('1')]

for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
        compare(mylist[i], mylist[j])

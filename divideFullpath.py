# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:35:02 2022

@author: yan-s
"""

import os

fullpath = r'C:/Users/yan-s/Documents/pypy/Location Geography & Co/Sine Saloum/repo/Sine Saloum 2.0.kml'

dirname, fname = os.path.split(fullpath)

dirname = dirname+'/'

print(dirname)
print(fname)
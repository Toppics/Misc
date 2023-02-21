# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 12:28:02 2022

@author: yan-s
"""
import os

def latestDirectory(path):
    # Get the latest directory
    latest = sorted([d for d in os.listdir('.') if os.path.isdir(d)], 
                    key=lambda x: os.path.getctime(x), reverse=True)[:1]
    return latest
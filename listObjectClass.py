# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:01:02 2022

@author: yan-s
"""

class LOB: 
    def __init__(self, name, roll): 
        self.name = name 
        self.roll = roll
   
# creating list       
list = [] 
  
# appending instances to list 
list.append( LOB('Barout', 22) )
list.append( LOB('Aarpax', 4) )
list.append( LOB('Gloria', 65) )
  
for obj in list:
    print( obj.name, obj.roll, sep =' ' )
  

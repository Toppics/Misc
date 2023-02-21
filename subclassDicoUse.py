# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:05:02 2022

@author: yan-s
"""

"""input un Dico de dico
for dico in Dico create object + add to list
for object in list, plot


"""

class ClassName:
    def __init__(self, dico):
        for x in dico:
            self.plot(ClassName.foo(**x))
            
    def plot(self, arg):
        print(arg)
        
    class foo:
        def __init__(self, Dico):
            print(Dico)
        
        
if __name__ == '__main__':
    dico = [
        {'Dico': 'Param1'},
        {'Dico': 'Param2'},
        {'Dico': 'Param3'}        
        ]
    
    exeSeq = ClassName(dico)
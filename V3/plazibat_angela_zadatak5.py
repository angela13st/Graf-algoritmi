# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:23:02 2023

@author: Student
"""

def funkcija(dict):
    novi={}
    for klj, vrij in dict.items():
        for v in vrij:
            if v not in novi:
                novi[v]=[]
            novi[v].append(klj)
    return novi


d = {
     1:[2,3,5],
     2:[1, 4], 
     3:[1,2]
     }

novi=funkcija(d)
print(novi)
    
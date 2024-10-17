# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:58:51 2023

@author: Student
"""


def presjek(l1,l2):
    return set(l1).intersection(l2)


l1=[1,2,3,4,5,6,7,8,9]
l2=[3,6,9,12]
l3=presjek(l1, l2)

print(l3)


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:27:46 2023

@author: Student
"""

a=float(input('Unesi a:'))
b=float(input('Unesi b:'))
c=float(input('Unesi c:'))
d=float(input('Unesi d:'))

if(b<c or d<a):
    print('[prazan skup]')
else:
    pocetak=max(a,c)
    kraj=min(b,d)
    print('[', pocetak,',', kraj, ']')
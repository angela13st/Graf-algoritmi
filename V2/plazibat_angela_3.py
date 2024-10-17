# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:58:10 2023

@author: Student
"""
def samoglasnici(s):
    br=0
    for i in range(1,len(s)):
        if((s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u') and (s[i-1]=='a' or s[i-1]=='e' or s[i-1]=='i' or s[i-1]=='o' or s[i-1]=='u')):
            br+=1
    return br
    

s=input('Unesi string:')
print(samoglasnici(s))
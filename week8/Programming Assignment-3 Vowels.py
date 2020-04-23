# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 06:02:17 2019

@author: cheerag.verma
"""
#text='your article is in queue'
text = input()
vowel =['a','e','i','o','u']
flag = 0
newstring=""
for data in text:
    if data not in vowel:
        newstring = newstring+data
        flag = 0
        
    elif data in vowel:
        if flag == 0:
            newstring = newstring +data
            flag=1
        else:
            flag=1
    else:
        pass

print(newstring)

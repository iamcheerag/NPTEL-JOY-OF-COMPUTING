# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:52:57 2019

@author: cheerag.verma
"""

d={}

def printDict(n):
    for i in range(n):
        d[i+1]=(i+1)*(i+1)
    print(d)
    
n = int(input())
printDict(n)
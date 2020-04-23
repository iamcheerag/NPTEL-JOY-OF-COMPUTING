# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:42:18 2019

@author: cheerag.verma
"""
d={}

def cube(n):
    for i in range(n):
        d[i+1]=(i+1)*(i+1)*(i+1)
    print(d)
    
n = int(input())
cube(n) 
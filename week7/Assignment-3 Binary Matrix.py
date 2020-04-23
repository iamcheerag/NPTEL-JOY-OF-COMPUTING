# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:50:40 2019

@author: cheerag.verma
"""

r,c = map(int,input().split())
counter =0
b=[]

for i in range(r):
    b.append([int(j) for j in input().split()])

for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j] == 0 or b[i][j] ==1:
            counter +=1

if counter==r*c:
    print("YES")
else:
    print("NO")
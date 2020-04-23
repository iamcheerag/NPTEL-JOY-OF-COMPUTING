# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:54:18 2019

@author: cheerag.verma
"""
n=int(input())
a=[]
count=0

for i in range(n):
    a.append([int(x) for x in input().split()])
    
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==a[j][i]:
            count+=1
            
            
if count == n*n:
    print("YES")
else:
    print("NO")
    
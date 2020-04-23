# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:29:12 2019

@author: cheerag.verma
"""

x = list(map(int,input().split(" ")))
n = len(x)
for i in range(n):
    for j in range(0, n-i-1):
        if x[j] == 0:
            x[j], x[j+1] = x[j+1], x[j] 

count = 1
for data in x:
    if count < len(x):
        print(data,end = " ")
        count = count +1
    else:
        print(data,end="")
        
        
        
import numpy as np
i = ([1,2,3,4],[1,2,3,4])
type(np.asanyarray(i))

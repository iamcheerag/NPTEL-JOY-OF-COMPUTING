# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:02:32 2019

@author: cheerag.verma
"""

import random
original_list = []
new =''
n = int(input())
for i in range(0,n):
    element = int(input())
    original_list.append(element)

new_list = original_list.copy()
original_list.sort()

while(original_list != new_list):
    idx1 = random.randint(0,len(new_list)-1)
    idx2 = random.randint(0,len(new_list)-1)
    new_list[idx1],new_list[idx2] = new_list[idx2],new_list[idx1]
    if (new_list == original_list):
        for r in range(n):
            if(r<n-1):
                print(new_list[r],end=" ")
            else:
                print(new_list[r],end='')
       
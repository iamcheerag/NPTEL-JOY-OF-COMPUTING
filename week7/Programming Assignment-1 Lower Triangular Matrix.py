# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:32:47 2019

@author: cheerag.verma
"""
n = int(input())  # depicts number of rows of the matrix

list_=[]
for i in range(n):
  list_.append([int(j) for j in input().split()])

for row in range(n):
  for col in range(n):
    if row<col:
      list_[row][col]=0
     

for row in range(len(list_)):
    y=n 
    for col in range(len(list_[row])):
        if y!=1:
            print(list_[row][col],end=" ")
            
        if y==1:
            print(list_[row][col],end="")
        
        y=y-1
    
    if(y!=1):
        print()
    
    

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:22:11 2019

@author: cheerag.verma
"""

def spiral(row,col,mat):	
    row_index = 0
    col_index = 0
    
    while(row_index < row and col_index < col):
        
        for i in range(row_index,row):
            print(mat[i][col_index],end = " ")
        col_index+=1
        
        for i in range(col_index,col):
            print(mat[row-1][i],end = " ")
        row-=1
   
        for i in range(row-1,row_index-1,-1):
            print(mat[i][col-1], end = " ")
        col = col-1
        
        for i in range(col-1,col_index-1,-1):
            print(mat[row_index][i],end = " ")
        row_index = row_index + 1

a=[]

n = int(input())
b=[]
for i in range(n):
    b.append([int(j) for j in input().split()])

spiral(n,n,b)
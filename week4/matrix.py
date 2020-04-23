# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:41:52 2019

@author: cheerag.verma
"""
"""
You are provided with the number of rows (R) and columns (C). Your task is to generate the matrix having R rows and C columns such that all the numbers are in increasing order starting from 1 in row wise manner.

Input Format:
The first line contain two numbers R and C separated by a space.

Output Format:
Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.

NOTE: There should not be any space after the last element of each row and no new line after the last row.

Example:

Input:
3 3

Output:
1 2 3
4 5 6
7 8 9

Explanation: 
Starting from the first row, the numbers are present in the increasing order. Since it's a 3X3 matrix, the numbers are from 1 to 9
"""


r,c = map(int,input().split(" "))
y=0
l2=[]
counter = 1
for i in range(r):
    l1=[]
    for j in range(c):
        l1.append(counter)
        counter=counter+1
    l2.append(l1)

for row in l2:
    print(' '.join(str(n) for n in row))
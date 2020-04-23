# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:05:39 2019

@author: cheerag.verma
"""
'''
Given a list of numbers (integers), find second maximum and second minimum in this list.

Input Format:

The first line contains numbers separated by a space.

Output Format:

Print second maximum and second minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

4 2 
'''
mylist = list(map(int,input().split()))
mylist.sort()
print(mylist[-2],end=" ")
print(mylist[1],end = "")


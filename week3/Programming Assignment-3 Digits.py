# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:05:40 2019

@author: cheerag.verma

You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

Input Format:

The first line contains a number made up of 0's and 1's.

Output Format:

Print 'YES' or 'NO' accordingly without quotes.

Example:

Input:

101

Output:
YES

Explanation: 
If you flip the middle digit from 0 to 1 then all the digits will become same. Hence output is YES. """

a = int(input())
b = str(a)
countofzero = b.count('0')
countofone = b.count('1')   
if countofzero ==1 or countofone == 1:
     print("YES",end= "")
else:
    print("NO",end="")


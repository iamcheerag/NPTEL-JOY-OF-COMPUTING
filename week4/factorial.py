# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:30:41 2019

@author: cheerag.verma
"""
"""
Given an integer number n, you have to print the factorial of this number

Input Format:
A number n.

Output Format:
Print the factorial of n.

Example:
Input:
4

Output:
24 

"""

def factorial(n):
    fact = 1

    for i in range(n):
        fact = fact * (i+1) 
    return fact

n = int(input())
factorial_of_number = factorial(n)
print(factorial_of_number,end="")

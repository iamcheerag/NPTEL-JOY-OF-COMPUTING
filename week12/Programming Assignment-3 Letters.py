# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:45:28 2019

@author: cheerag.verma
"""
import string
#letter = 'Python is an interpreted high-level programming language'
letter = input()
countSmallLetter = 0
countCapitalLetter = 0
for i in letter:
    if i in string.ascii_lowercase:
        countSmallLetter= countSmallLetter+1
    elif i in string.ascii_uppercase:
        countCapitalLetter = countCapitalLetter+1
    else:
        pass
print(countCapitalLetter,countSmallLetter)
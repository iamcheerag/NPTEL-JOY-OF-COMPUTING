# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:31:01 2019

@author: cheerag.verma
"""
holes_dict = {"A":1,"B":2,"C":0,"D":1,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":1,"P":1,"Q":1,"R":1,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
import string
text = "CHEERAG VERMA"
#text = input()
sum = 0
for i in text:
    #print(i,holes_dict[i])
    if i in string.ascii_uppercase:
        sum  = sum +holes_dict[i]
    else:
        pass
print(sum)
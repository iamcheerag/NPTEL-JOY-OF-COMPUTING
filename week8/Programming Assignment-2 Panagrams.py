# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:47:09 2019

@author: cheerag.verma"""
import string
l=input()

l=l.lower()
d={}
for i in range(len(l)):
#    if i<len(l)-1:
#        j=i+1
#    else:
#        break
    count = 0
    for j in range(len(l)):
        if l[i] in string.ascii_letters:
            if l[i]!=l[j]:
                d[l[i]] = count
            else:
                count+=1
                d[l[i]]=count
        else:
            pass

sorted(d.items(),key = lambda x:x[0])

if len(d)==26:
    print("YES")
else:
    print("NO")



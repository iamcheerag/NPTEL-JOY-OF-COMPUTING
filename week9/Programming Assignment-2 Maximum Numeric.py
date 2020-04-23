# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:06:35 2019

@author: cheerag.verma
"""
#
#import string
#flag = 0
#s = '12abc23bfd6fdsa'
#a=[]
#b=[]
#
#for i in range(len(s)):
#    if s[i] in string.ascii_lowercase:
#        b.append(s[i])
#    else:
#        #print("i:",i)
#        idx = i
#        #print("idx:",idx)
#        while(idx<len(s)):
#            #print("idx1:",idx)
#            if s[idx] not in string.ascii_lowercase:
#                #print("s[idx]:",s[idx])
#                a.append(int(s[idx]))
#                idx+=1
#            else:
#                break
#        print()
#        
#a.sort()
#print(a[-1])
#


import re
s ='12abc23bfd6fdsa'
x = re.sub(r'[A-z]',' ',s)

s1=x.split()
s2 = [int(i) for i in s1 ]
s2.sort()
print(s2[-1])



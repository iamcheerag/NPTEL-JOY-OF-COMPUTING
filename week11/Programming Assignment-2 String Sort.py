# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:09:48 2019

@author: cheerag.verma
"""

inputName = list(map(str,input().split(",")))

#dict_name = {}
#count = 1
#for i in inputName:
#    dict_name[i] = count
#    count+=1
#    
#sorted_list = sorted(dict_name.items(),key = lambda x:x[0])
#
#x = 1
#for data in sorted_list:
#    if x<len(sorted_list):
#        print(data[0],end=",")
#        x+=1
#    else:
#        print(data[0])
        
        
sorted_list = sorted(inputName)

x = 1
for data in sorted_list:
    if x<len(sorted_list):
        print(data,end=",")
        x+=1
    else:
        print(data)
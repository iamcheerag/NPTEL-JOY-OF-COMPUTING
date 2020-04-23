# -*- coding: utf-8 -*-

def time(n,velocity_of_arun,velocity_of_cab):
    
    timeTakenByArun = (1.41* n)  / velocity_of_arun
    
    timeTakenByCab = (2 * n) / velocity_of_cab
    
    if timeTakenByCab > timeTakenByArun :
        print("Walk")
    else:
        print("Cab")
        
n= 0 
va= 0
vc = 0    
n,va,vc = input().split()    
n = int(n)
velocity_of_arun = int(va)
velocity_of_cab  = int(vc)

time(n,velocity_of_arun,velocity_of_cab)
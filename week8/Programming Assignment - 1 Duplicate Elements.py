
l1=[1,1,2,3,4,5,5]
l2=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
    else:
        pass

listToStr = ' '.join([str(elem) for elem in l2]) 
print(listToStr)

for el in l2:
    print("".join(str(el)),end=" ")
    
            
        
        
        
        
        
        
        
        
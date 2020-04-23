n = int(input())
mylist = list(map(int,input().split()))
cp_pos = int(input())

element = mylist[cp_pos-1]
mylist.sort()

print(mylist.index(element)+1)
#for i in range(len(mylist)):
#    if mylist[i] == element:
#        print(i+1)
#        break
#    
    
    

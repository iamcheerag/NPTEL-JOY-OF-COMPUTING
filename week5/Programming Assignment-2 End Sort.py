myList = list(map(int,input().split()))
sortedList = sorted(myList)
count = 0
for i in range(len(myList)):
    if myList[i] ==  sortedList[count]:
        count = count+1
print(len(myList)-count,end = " ") 


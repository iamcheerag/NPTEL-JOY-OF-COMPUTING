# =============================================================================
# 
# a=[]
# b=[]
# #m=4
# n,m = map(int,input().split())
# #m = int(input())
# #mylist = [5 ,1 ,8, 3, 9 ,2 ,13 ,23, 4 ,9]
# mylist = list(map(int,input().split()))
# mylist.sort()
# #print(mylist)
# i=0
# while(i<len(mylist)-m+1):
#     for j in range(i,m+i):
#         a.append(mylist[j])
#         a.sort()
#     b.append(a.copy())
#     #print(b)
#     a.clear()
#     i+=1 
# 
# list_of_min=[]
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         minimum = abs(b[i][j]-b[i][m-1])
#         list_of_min.append(minimum)
#         break
#         
# print(min(list_of_min))
# 
# =============================================================================

n,m = map(int,input().split())
a = list(map(int,input().split()))
def calculatemindiff(n,m,a):
    j=0
    a.sort()
    result=[]
    for i in range(len(a)-m+1):
        #print(a[i:j+m])
        temp=a[i:j+m]
        mindiff=temp[-1]-temp[0]
        result.append(mindiff)
        j=j+1
    result.sort()
    return result[0]

answer=calculatemindiff(n,m,a)
print(answer,end = "")

import math
C = 50
H = 30

D = list(map(int,input().split(",")))

for i in range(len(D)):
    Q = round(math.sqrt((2*C*D[i])/H))
    if i<len(D)-1:
        print(Q,end = ",")
    else:
        print(Q,end = "")
	
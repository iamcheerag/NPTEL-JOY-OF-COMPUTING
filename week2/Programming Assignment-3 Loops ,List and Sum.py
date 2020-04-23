n = int(input())
a = list(map(int , input().split()))
b = a[::-1]
c = []

for i in range(n):
    c.append(a[i]+b[i])
print(" ".join(map(str,c)),end="")
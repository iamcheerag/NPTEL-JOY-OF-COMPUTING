import functools
x = int(input())
def factorsOfElement(x):
    factors = []
    notPrime = []
    for i in range(2,x+1):
        if x % i == 0 :
            factors.append(i)
            for j in range(2,i):
                if(i%j == 0):
                    notPrime.append(i)
                    break
    factorSet = set(factors)
    notPrimeSet = set(notPrime)
    mul = factorSet.difference(notPrime)
    return mul


flag = False
for i in range(2,x):
    primefactor1 = factorsOfElement(i)
    primefactor2 = factorsOfElement(x-i)
    if len(primefactor1) ==1 or len(primefactor2) == 1:
        continue
    result1 = functools.reduce(lambda a,b:a*b ,list(primefactor1))
    result2 = functools.reduce(lambda a,b:a*b,list(primefactor2))
    if result1+result2 == x:
      flag = True
      break
    else:
        pass
        
if flag:
    print('Yes',end ="")
else:
    print('No',end = "")
    
    
#NOTE: THIS WILL NOT PASS THE SECOND TEST CASE, HAVENOT FIGURED OUT THE WAY, WILL UPDATE SOON.
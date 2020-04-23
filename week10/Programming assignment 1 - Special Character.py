import string

s = input()
flag = 0
for i in s:
    if i == " " or i in string.digits:
        continue
    if not i in string.ascii_letters:  #identifying special character
        flag =  1
        break
    
if flag == 1:
    print("YES",end = "")
else:
    print("NO",end = "")
    
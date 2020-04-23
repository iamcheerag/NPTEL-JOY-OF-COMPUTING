str1 = 'Cheerag'
str2 = 'Kriti'

name1 = str1.lower()
name2 = str2.lower()

name1 = list(name1)
name2 = list(name2)


for i in range(len(name1)):
    for j in range(len(name2)):
        print(i,j)
        if name1[i] == name2[j]:
            c = name1[i]
            print(c)
            name1.remove(c)
            name2.remove(c)
            break
print(name1,name2)
        
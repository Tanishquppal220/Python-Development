l = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)
print(len(l))
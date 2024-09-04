l=input("enter a list")

d={}
for i in l:
    if i not in d and i.isspace()==False:
        d[i]=1
    elif i in d:
        d[i]+=1
print(d)
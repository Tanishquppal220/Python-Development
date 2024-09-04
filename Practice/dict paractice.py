print('1:To Count no of Charachters','2:To Count no of word',sep="\n")
index=eval(input("Enter index of progam(1 to 4): "))

if index==1:
    s=input("Enter a string: ")
    s=s.upper()
    d={}
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
        

elif index==2:
    s=input("Enter a string: ")
    s=s.upper()
    s=s.split()
    d={}
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)

elif index==3:
    s=input("Enter a string: ")
    s=s.upper()
    s=s.split()
    d={}
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)





'''
#range of a list
elif index==4:
    s=eval(input("Enter a list: "))
    r=max(s)-min(s)
    print(r)
'''

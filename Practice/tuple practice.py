#To print cube of every 3rd element of tuple
index=eval(input("Enter index of progam(1 to 4): "))
if index==1:
    s=eval(input("Enter a tuple: "))
    for i in range(2,len(s),3):
        print(s[i]**3)


#TO print a tupke with every 3rd element of first
elif index==2:
    s=eval(input("Enter a tuple: "))
    l=[]
    for i in range(2,len(s),3):
        l.append(s[i])
    print(tuple(l))



#To enter n numbers and print tuple of n, 2n,3n,4n numbers
elif index==3:
    s=eval(input("Enter a number: "))
    l=[]

    for i in range(1,5):
        l.append(s*i)

    l=tuple(l)
    print(l)



#range of a list
elif index==4:
    s=eval(input("Enter a list: "))
    r=max(s)-min(s)
    print(r)

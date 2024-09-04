def lenWords(a):
    t=[]
    a=a.split()
    for i in a :
        t.append(len(i))
    return tuple(t)
x=input("Enter a String:")
print(lenWords(x))

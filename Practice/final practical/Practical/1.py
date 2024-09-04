x=input("Enter the string: ")
def lenstring(x):
    t=[]
    l=x.split()
    for i in l:
        t.append(len(i))
    print(t)
lenstring(x)

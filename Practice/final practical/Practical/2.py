l=eval(input("Enter first list:"))
m=eval(input("Enter Second list:"))
if len(m)==len(l):
    n=[]
    for i in range(0,len(l)):
        n.append(l[i]+m[i])
    print(n)
else:
    print("Enter lists of same length")
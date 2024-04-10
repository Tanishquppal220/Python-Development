r=int(input("Enter Number of row you want to print: "))
n= bool(int(input("Enter 1 Or 0: ")))
if n==True:
    for i in range(1,r+1):
        print("*"*i)
else:
    for i in range(r,0,-1):
        print("*"*i)

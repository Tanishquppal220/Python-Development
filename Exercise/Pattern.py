r=int(input("Enter Number of row you want to print:\n"))
n= int(input("Enter 1 Or 0:\n"))
n2= bool(n)
# print(n2)
'''
if n2==True:
    for i in range(1,r+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif n2==False:
    for i in range(r,0,-1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
'''
if n==True:
    for i in range(1,r+1):
        print("*"*i)
elif n==False:
    for i in range(r,0,-1):
        print("*"*i)

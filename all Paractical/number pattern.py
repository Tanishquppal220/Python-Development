a = int(input("Enter the number:"))
for i in range(a,0,-1):
    for j in range(1,i+1):
        print(j,sep=" ",end=" ")
        j=j-1
    print()




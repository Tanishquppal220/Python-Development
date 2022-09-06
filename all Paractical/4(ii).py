a = int(input("Enter the number:"))

print("from 1 to", a)
for i in range(0,a+1):
    for j in range(1,i+1):
        print(j,sep=" ",end=" ")
        j=j+1
    print()
print("================================================================")
print("from", a, "to 1")
for i in range(a,0,-1):
    for j in range(1,i+1):
        print(j,sep=" ",end=" ")
        j=j-1
    print()


n = []
while True:
    # Give input in form [1,2,4]
    l = eval(input("Enter a list of number:"))
    m = eval(input("Enter a list of number:"))
    if len(l) == len(m):
        for i in range(0, len(l)):
            n.append(l[i]+m[i])
        break
    else:
        print("Enter same number of elements in both the list")
        continue
print("Sum Of list is:", n)
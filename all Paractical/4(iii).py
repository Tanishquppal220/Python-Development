a = int(input("Enter the number of rows:"))
b=65
for r in range(0,a+1):
    for c in range(b, b+r):
        print(chr(c), sep=" ", end=" ")
        c = c+1
    print()

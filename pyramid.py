a = int(input("Enter the number of rows: "))
for i in range(0, a + 1):
    print(" " * (a - i), end=" ")
    for j in range(0, i):
        print(j + 1, sep=" ", end=" ")
    print()

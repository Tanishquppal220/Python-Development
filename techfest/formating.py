n = int(input("Enter the number of rows: "))
# n=4
for i in range(1, n + 1):
    print("*" * (n - i+1), end="")
    for j in range(1, i):
        print(" ", end=" ")
    print("*" * (n - i+1))
for i in range(1, n):
    print("*" * (i+1), end="")
    for j in range(1, n-i):
        print(" ", end=" ")
    print("*" * (i+1))

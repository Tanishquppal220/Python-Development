a = int(input("Enter the number of rows: "))
b = int(input("Enter the number of columns: "))
for i in range(0, a):
    for j in range(0, b):
        if i == 0 or i == a - 1 or j == 0 or j == b - 1:
            print("*", end="  ")
        else:
            print("  ", end=" ")
    print()

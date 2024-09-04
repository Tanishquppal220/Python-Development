x = int(input("Enter the first Number: "))
y = int(input("Enter the Second Number: "))

if x % y == 0:
    print(y)
for k in range(int(y / 2), 0, -1):
    if x % k == 0 and y % k == 0:
        hcf = k
        print(hcf)
        break
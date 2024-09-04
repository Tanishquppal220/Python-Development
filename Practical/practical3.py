a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))
if a > b and a > c:
    print(a, "is greatest")
elif b > a and b > c:
    print(b, "is greatest")
elif c > a and c > b:
    print(c, "is greatest")

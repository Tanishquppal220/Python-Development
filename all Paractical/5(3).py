x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sum=0
for i in range(1, n + 1):
    term = x ** i / i
    if i%2==0:
        sum -=term
    else:
        sum += term
print("Sum =", sum)


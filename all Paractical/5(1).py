x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sum=1
for i in range(1, n + 1):
    term = x ** i
    sum +=term
print("Sum =", sum)
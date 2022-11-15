# a = int(input("Enter the first term: "))
# b = int(input("Enter the Second term: "))
a=1
b=1
n = int(input("Enter the Total number of term: "))
sum = a+b
print(a, b, end=" ")
i = 3
while i <= n:
    c = a+b
    print(c, end=" ")
    a = b
    b = c
    i = i+1


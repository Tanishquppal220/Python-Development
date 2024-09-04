a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if a>b:
    while b:
        a,b=b,a%b
    print(a)

else:
    while a:
        b,a=a,b%a
    print(b)
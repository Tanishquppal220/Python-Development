# program to identify amstrong number

num = int(input("Enter a number: "))
s = 0
temp = num
while temp > 0:
    digit = temp % 10
    s += digit**3
    temp //= 10
if s == num:
    print("It is an amstrong number")
else:
    print("It is not an amstrong number")

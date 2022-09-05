# For print from 1 star to a stars

a = int(input("Enter the number:"))

i=0
print("From 1 to",a)
while i<=a:
    print("*"*i)
    i = i+1
print("--------------------------------")

# For print from a star to 1 stars
print("From",a," to 1")

while a >= 1:
    print("*"*a)
    a = a-1

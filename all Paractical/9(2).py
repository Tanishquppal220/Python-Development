x = int(input("Enter the first Number:"))
y = int(input("Enter the Second Number:"))
if x < y:
    g = y
elif y < x:
    g = x
while(True):
    if g%x==0 and g%y==0:
        print(g)
        break
    g=g+1


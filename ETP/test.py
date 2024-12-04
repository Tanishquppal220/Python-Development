def t(x):
    if x%2==0:
        return "yes"
    else:
        return False

a="1,2,3,4,5,6".split(",")
y=lambda x:x%2==0
c=list(map(int,a))
b=list(filter(t,c))
d=list(map(t,c))
print(b)
print(d)
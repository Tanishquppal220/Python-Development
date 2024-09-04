d={}
n=int(input("Entar total no of entries: "))

for i in range(n):
    r=eval(input("Enter roll no: "))
    m=eval(input("Enter marks: "))
    name=(input("Enter Name: "))
    d[r]=[name,m]
print(d)
for i in d:
    if d[i][1]>75:
        print(d[i])

f=open(r"C:\Users\dell\Desktop\School-work\Tanishq\Development\School-Class-12\Term 1\Files\Assignement 1\Q2.txt","r+")
a=f.readlines()
l=[]
for i in a:
    l+=i.split()
b=""
for i in l :
    if i!=l[len(l)-1]:
        b=b+i+"#"
    else:
        b=b+i
print(b)
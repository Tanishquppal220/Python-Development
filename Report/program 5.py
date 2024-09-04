import pickle as p
f = open(r"program_5.dat", "rb")
try:
    while True:
        print(p.load(f))
except EOFError:
    f.close()
f=open(r"program_5.dat","rb")
l=[]
try:
    while True:
        a=p.load(f)
        l.append(a)
except EOFError:
    f.close()
rno=int(input("Enter roll number of student:"))
for i in l:
    if i[0]==rno:
        i[2]=int(input("Enter new marks:"))
        break
f=open(r"program_5.dat","wb")
for i in l:
    p.dump(i,f)
f.close()
f=open(r"program_5.dat","rb")
try:
    while True:
        print(p.load(f))
except EOFError:
    f.close()

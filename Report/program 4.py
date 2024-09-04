import pickle as p
# c=True
# while c==True:
#     print("===================Menu===================")
#     print("1.Write in file")
#     print("2.Read from file")
#     print("3.Search in File")
#     print("4.Exit")
#     ch=int(input("Enter your choice:"))
#     if ch==1:
#         f=open(r"program_4.dat","wb")
#         n=int(input("Enter number of students:"))
#         for i in range(n):
#             rno=int(input("Enter roll number:"))
#             name=input("Enter name:")
#             l=[rno,name]
#             p.dump(l,f)
#         f.close()
#     elif ch==2:
#         f=open(r"program_4.dat","rb")
#         try:
#             while True:
#                 l=p.load(f)
#                 print(l)
#         except EOFError:
#             f.close()
#     elif ch==3:
#         f=open(r"program_4.dat","rb")
#         rno=int(input("Enter roll number to be searched:"))
#         try:
#             while True:
#                 l=p.load(f)
#                 if l[0]==rno:
#                     print(l)
#                     break
#         except EOFError:
#             print("No Record Found")
#             f.close()
#     elif ch==4:
#         c=False
# ! Finally:
f = open(r"program_4.dat", "rb")
print("Input is :")
try:
    while True:
        l = p.load(f)
        print(l)
except EOFError:
    f.close()
c = "y"
while True:
    f = open(r"program_4.dat", "rb")
    rno = eval(input("Enter roll number to be searched:"))
    try:
        while True:
            l = p.load(f)
            if l[0] == rno:
                print(l)
                break
    except EOFError:
        print("No Record Found")
        f.close()
    c = input("Do you want to continue(y/n):")
    if c == "n":
        break

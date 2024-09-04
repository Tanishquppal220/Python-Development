import pickle as p
# f = open("File Handling\\binary.dat","ab")
# while True:
#     i=eval(input("Enter anything: "))
#     p.dump(i,f)
#     if i=="n":
#         break
# f.close()
f = open("File Handling\\binary.dat","rb")
try :
    a=p.load(f)
    for i in a :
        print(i)
except EOFError:
    pass
f.close()
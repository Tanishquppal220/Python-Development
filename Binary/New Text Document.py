import pickle
def write():
    f=open("file.dat","wb")
    li=eval(input("Enter a list: "))
    pickle.dump(li,f)
    print("Data entered")  
    f.close()
def read():
    f=open("file.dat","rb")
    li=pickle.load(f)
    print(li,type(li),sep="\n")
    f.close()

write()
read()

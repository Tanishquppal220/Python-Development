import pickle
file=open("binary.dat","wb+")
rec=[]
ans=""
while True:
    rollno=int(input("Enter Rollno"))
    name=input("Enter Name :")
    marks=int(input("Enter marks :"))
    data=[rollno,name,marks]
    rec.append(data)
    pickle.dump(data,file)
    ans=input("Do you want to continue ?(y/n)")
    if ans =='n':
        break
pickle.dump(rec,file)
file.seek(0)
f=pickle.load(file)
f2=pickle.load(file)
f3=pickle.load(file)
print(f,f2,f3,sep="\n")
file.close()
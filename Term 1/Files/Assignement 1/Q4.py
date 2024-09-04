import pickle
f=open(r"Assignement 1\Q4.dat","wb")
list=["computer","science","engineering"]
dict={"computer":1,"science":2,"engineering":3}
pickle.dump(list,f)
pickle.dump(dict,f)
f.close()
f=open(r"Assignement 1\Q4.dat","rb")
list=pickle.load(f)
print(list)

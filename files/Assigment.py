l=[]
b=[]
def longline():
    l=f.readlines()
    for i in range(0,len(l)):
        a=l[i].split()
        if len(a)>=7:
            print(l[i])
    
f=open('lines.txt',"r+")
longline()
f.close()

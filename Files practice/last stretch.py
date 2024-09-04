import pickle as p
'''
f=open(r"Text.txt","r+")
print(f.read())
f.close()
with open("Text2.txt", "r+") as f:
    print(f.readline().rstrip("\n"))
    print(f.readline())
'''
# TODO stdin stdout stderr
'''
a=s.stdin.read()
s.stdout.write(a)
'''
# TODO Binary file
'''
with open("binary.dat","rb+") as f:
    # p.dump("This is line number 2 of file.",f)
    f.seek(0)
    try:
        c=0
        while True:
            
            a=p.load(f)
            for i in a :
                if i not in "2":
                    print(i,end="")
                elif i in "2":
                    c+=1
                    break
                else:
                    pass
            if c==1:
                break
            else:
                pass
    except:
        pass
'''
# TODO CSV File
''''''
import csv as c
with open("Csv1.csv","a+",newline="") as f:
    w=c.writer(f)
    r=c.reader(f)
    a=eval(input("Enter a list"))
    w.writerow(a)
    f.seek(0)
    print(list(r))
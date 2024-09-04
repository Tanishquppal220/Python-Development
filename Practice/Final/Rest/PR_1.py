t=(1,2,3,[1,2,3,4],4)
print(t)
t[3].append(5)
print (t)
try:
    t[2]=1
    print(t)
except:
    print("Error")
t[3][0]=0
print(t)

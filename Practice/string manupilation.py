a=input("enter a string : ")
#This is for reversing
'''
print("Ths is string in reverse : ",a[::-1])
for i in range (1,len(a)+1):
    print(a[-i])
'''
v=['a','e','i','u','o','A','E','I','U','O']
l=list(a)
count=0
for i in range (0,len(l)):
    q=l[i]
    if q in v:
        count+=1
    else:
        continue
print(count)

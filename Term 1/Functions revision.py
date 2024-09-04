# This a functions
# !program 1
'''
def opr(a,d,b=5):
    add=a+b
    sub=a-b
    multi=a*b
    div=a/b
    return add,sub,multi,div,d
a=eval(input("Enter two numbers: "))
b=eval(input("Enter two numbers: "))
w,e,r,t,y=opr(a,b)
print(w,e,r,t,y,sep="\n")
'''
# ! program 2
'''
def incremant():
    global a 
    a=a+1
a=5
print(a)
incremant()
print(a)
'''
# ! program 3
def interest ( prin , time , rate ) :
    return prin * time * rate
print (interest ( prin = 2000 , rate=0.10 , time = 2 ))
'''
'''
def add(A):
    n=int(input('How many entries you want to make:'))
    if n!=0:
        for i in range(0,n):
            a=eval(input('Make a entry:'))
            A.append(a)
    print("--------------------------------------------------")

def remove(A):
    if len(l)==0:
            print("Stack is empty.....",end='\n\n')
    else:
        a=A.pop()
        print(a,"has been removed",end='\n\n')
    print("--------------------------------------------------")

def display(A):
    A=reversed(A)
    print(A,end='\n\n')
    print("--------------------------------------------------")
index=0
l=[]
while index != 4:
    print("1. Add a value")
    print("2. Display")
    print("3. remove")
    print("4. Exit",end='\n\n')
    index=int(input("What do you Want to do?"))
    print()
    if index==1:
        add(l)
    if index==2:
       display(l)
    if index==3:
        remove(l)
    






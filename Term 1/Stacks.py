def push(l,a):
    l.append(a)
    return l
def pop(l):
    if l==[]:
        print("Stack is empty")
    else:
        a=l.pop()
        print("popped element is :",a)
    return l
def display(l):
    if l==[]:
        print("Stack is empty")
    else:
        for i in l[::-1]:
            print(i)
def peek(l):
    if l==[]:
        print("Stack is empty")
    else:
        print("Top element is:",l[-1])




s=[1,2,3,4,5,7]
print("Initial stack is:",s[::-1])
choice='Y'
while choice=='Y' or choice=='y'or choice=="":
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peak")
    print("5. Exit")
    c=input("Enter your choice: ")
    if c=='1':
        a=eval(input('Enter element: '))
        s=push(s,a)
        display(s)
    elif c=='2':
        s=pop(s)
        display(s)
    elif c=='3':
        display(s)
    elif c=='4':
        peek(s)
    elif c=='5':
        break
    else:
        print("Wrong choice")
    choice=input("Do you want to continue? (Y/N): ")
else:
    print("*Thank you for using the program!*")
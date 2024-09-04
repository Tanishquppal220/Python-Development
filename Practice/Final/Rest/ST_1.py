s=[1,2,3,4,5]
ch='Y'
while ch=='Y':
    print('1.Push')
    print('2.Pop')
    print('3.Display')
    print('4.Exit')
    c=int(input("Enter your choice:"))
    if c==1:
        e=int(input("Enter element to push:"))
        s.append(e)
    elif c==2:
        if len(s)==0:
            print("Stack is empty")
        else:
            e=s.pop()
            print("Popped element is:",e)
    elif c==3:
        if len(s)==0:
            print("Stack is empty")
        else:
            for i in reversed(s):
                print(i)
    else:
        break
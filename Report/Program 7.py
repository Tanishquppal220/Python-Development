s = [1, 2, 3, 4, 5, 7]
d = s[::-1]
print("Initial stack is:", d)
choice = 'Y'
while choice == 'Y' or choice == 'y' or choice == "":
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peak")
    print("5. Exit")
    c = input("Enter your choice: ")
    if c == '1':
        a = eval(input('Enter element: '))
        s.append(a)
        print("The stack is: ", s[::-1])
    elif c == '2':
        if s == []:
            print("Stack is empty")
        else:
            print("deleted element is: ", s.pop())
    elif c == '3':
        if s != []:
            l = s[::-1]
            print("The stack contains:")
            for i in l:
                print(i)
        else:
            print("The stack is empty")
    elif c == '4':
        if s == []:
            print("Stack is empty")
        else:
            print("The top element is: ", s[-1])
    elif c == '5':
        break
    else:
        print("Wrong choice")
    choice = input("Do you want to continue? (Y/N): ")
else:
    print("*Thank you for using the program!*")

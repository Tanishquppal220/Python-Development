
cont = "y"
while (cont=="y"):
    a = int(input("Enter First Number:\n"))
    o = (input("Enter Oprator:\n"))
    b = int(input("Enter Second Number:\n"))
    if o=="+": 
        print("Your Answer is:\n"+str(a+b))
    elif o=="-": 
        print("Your Answer is:\n"+str(a-b))
    elif o=="*": 
        print("Your Answer is:\n"+str(a*b))
    elif o=="/": 
        print("Your Answer is:\n"+str(a/b))
    else:
        print("Invalid input")
    cont=input("Do you want to continue?\n")
    if (cont=="n"):
        print("Thank you!\n")
        break

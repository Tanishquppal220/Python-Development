a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))
o = (input("Enter Oprator:\n"))
if a==45 and b==3 and o=="*":
    print("Your Answer is \n"+str(555))
elif a==3 and b==45 and o=="*":
    print("Your Answer is \n"+str(555))
elif a==56 and b==9 and o=="+": 
    print("Your Answer is \n"+str(77))
elif a==9 and b==56 and o=="+": 
    print("Your Answer is \n"+str(77))
elif a==56 and b==6 and o=="/": 
    print("Your Answer is \n"+str(4))    
elif o=="+": 
    print("Your Answer is:\n"+str(a+b))
elif o=="-": 
    print("Your Answer is:\n"+str(a-b))
elif o=="*": 
    print("Your Answer is:\n"+str(a*b))
elif o=="/": 
    print("Your Answer is:\n"+str(a/b))


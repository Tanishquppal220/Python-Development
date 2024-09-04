import random as r 
c="y"
while c=="y":
    a=str(r.randint(1,6))
    print("Your Roll is : "+a)
    c=input("Enter do you want to continue? (y/n):")
    if c=="y":
        pass
    else:
        break


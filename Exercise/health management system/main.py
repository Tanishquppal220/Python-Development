def getdate():
    import datetime
    return datetime.datetime.now()
while True:
    a=input("Enter Your Name: ")
    b=input("Enter you want diet or excersise: " )
    c = "Exercise\\health management system\\{}_{}.txt".format(a, b)
    print("Enter 1 for logging the data")
    print("Enter 2 for retrieving the data")
    print("Enter 3 for deleting the data")
    d=int(input('Enter your choice: '))
    if d==1:
        e=input("Enter the data: ")
        with open(c,'a') as f:
            f.write(str([str(getdate())])+": "+e+"\n")
    elif d==2:
        with open(c,"r") as f:
            print(f.read())
    elif d==3:
        with open(c,"w") as f:
            f.write("")


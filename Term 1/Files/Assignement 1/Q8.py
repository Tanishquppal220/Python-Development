l=eval(input("Enter a list of numbers: "))
stack=[]
for i in l:
    if i%5==0:
        stack.append(i)
    else:
        pass
if len(stack)==0:
    print("No numbers are divisible by 5")
else:
    print("Numbers divisible by 5 are: ",stack)
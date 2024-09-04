# l=eval(input("Enter a list :"))
l=[1,2,3,4,5,6,7,8,9,10]
s=eval(input("Search :"))
if s in l:
    print("Found at ","l[",l.index(s),']', sep="")
else:
    print("Not found")
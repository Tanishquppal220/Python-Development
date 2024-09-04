f = open(r"School-Class-12\Files practice\Text.txt", "r")
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# c=a+b
# f.write("A = "+str(a)+"\n")
# f.write("B = "+str(b)+"\n")
# f.write("C = "+str(c)+"\n")
# d=["sum"," of 2 numbers is ",str(c),"\n"]
# f.writelines(d)
# f.close()
# f=open("Text.txt","r")
# print(f.read())
# f.seek(0)
# x=f.readlines()
# length=0
# for i in range(0,len(x)) :
#     d=x[i]
#     d=d.rstrip("\n")
#     print(d)
#     length = length+len(d)
# print("Length of the file is: ",length)
print(f.read(2))
print(f.read(2))
print(f.read(2))



f.close()

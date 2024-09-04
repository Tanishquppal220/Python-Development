import csv
# f=open("Q7.csv","w",newline="")
# fw=csv.writer(f)
# rec=[]
# ans=""
# while True:
#     u=input("Enter Username :")
#     p=input("Enter Password :")
#     data=[u,p]
#     fw.writerow(data)
#     ans=input("Do you want to continue? (y/n)")
#     if ans=="n":
#         break
# f.close()
f=open("Q7.csv","r")
fr=csv.reader(f)
find=input("Enter Username to find :")
for i in fr:
    if i[0]==find:
        print("Username Found")
        print(i)
        break
    else:
        print("Username not found")

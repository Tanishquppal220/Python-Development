f=open(r"Files practice\database.txt","a+")
# n=int(input("Enter number of students: "))
# for i in range(0,n):
#     name=input("Enter name: ")
#     roll=input("Enter roll number: ")
#     marks=input("Enter marks: ")
#     l=["Name:",name,"\n","Roll No:",roll,"\n","Marks:",marks,"\n================================================================\n"]
#     f.writelines(l)

f.seek(0)
x=f.readlines()
print(x)
count=0
for line in x:
    line=line.split()
    # print(line)
    for i in line:
        # print(i)
        i=list(i)
        # print(i)
        if i[len(i)-1].isdigit():
            count+=1
print("Number of words with a number at last index:",count)
f.close()
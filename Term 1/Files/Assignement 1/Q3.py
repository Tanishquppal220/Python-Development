f=open(r"Assignement 1\Q3_2.txt","r+")
a=f.readlines()
l=[]
for i in a:
    for j in i:
        if j=="a":
            l.append(i)
            a.remove(i)
            continue
        else:
            pass
print(a)
with open(r"Assignement 1\Q3_2.txt","w") as f:
    f.writelines(a)
with open(r"Assignement 1\Q3.txt","a") as f:
    f.writelines(l)

# with open(r"Assignement 1\Q3_2.txt", "r+") as f:
#     lines = f.readlines()
#     lines_with_a = [line for line in lines if "a" in line]
#     lines_without_a = [line for line in lines if "a" not in line]

# with open(r"Assignement 1\Q3_2.txt", "w") as f:
#     f.writelines(lines_without_a)

# with open(r"Assignement 1\Q3.txt", "a") as f:
#     f.writelines(lines_with_a)

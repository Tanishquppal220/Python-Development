f=open(r"Text file.txt","r+")
a=f.read()
f.close()
c=""
for i in a.split("\n"):
    for j in i.split():
        c+=j+"#"
    c+=".\n\n"
print(c)

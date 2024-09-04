f=open("STORY.txt","r+")
l=f.readlines()
count=0
for i in l:
    if i[0] in "Aa":
        count+=1
    else:
        pass
print (count)

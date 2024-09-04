f=open('File Handling/text.txt','r')
a=f.readlines()
for i in a :
    if i.startswith('This') :
        print(i)
    # # print(i)
    # b=i.split(" ")
    # for j in b :
    #     print(j
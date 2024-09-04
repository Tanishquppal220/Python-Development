# ch=list(input("Enter a Word: "))
# alpha=0
# digit=0
# special=0
# for i in ch:
#    if i.isalpha():
#         alpha+=1
#    elif i.isdigit():
#         digit+=1
#    else:
#         special+=1
# print("Alphabets: ",alpha," Digits: ",digit," Special Characters: ",special)

#!ch.lstrip() is used to remove the any Character from the left side of the string
# ch ="aaaahhhhhaaaahhhhaaaa"
# a=ch.strip("a")
# print(a)
# b=a.count("h")
# print(b)

#!Important program It is used to count the number of words in a string by using count() function
# a=input("Enter a String: ")
# a=a.upper()
# d={'Total Alphabets':0,'Total Digits':0,'Total Special Characters':0}
# for i in range(0,122):
#     b=chr(i)
#     if b in a:
#         d[b]=a.count(b)
# for i in d:
#     if i.isalpha():
#         d['Total Alphabets']+=d[i]
#     elif i.isdigit():
#         d['Total Digits']+=d[i]
#     else:
#         d['Total Special Characters']+=d[i]
# for i in d:
#     print(i,"=",d[i],end=",")

a=input("Enter a String: ")
a.replace(" ",".")
for i in range(0,len(a),2):
    print(a[i:i+2])
    
# a="Hello World"
# print(a[0:len(a)+6], end=" ")
# print(a.upper().lower())



    

f = open(r"Term 1\Files\Assignement 1\Q2.txt", "r+")
a=f.read()
b=a.split()
vowels=0
consonats=0
upercase=0
lowercase=0
digits=0
def ul(j):
    global upercase,lowercase
    if j.isupper():
        upercase+=1
    elif j.islower():
        lowercase+=1
def vc(j):
    global vowels,consonats,digits
    if j in ["a","e","i","o","u","A","E","I","O","U"]:
            vowels+=1
    elif j not in ["a","e","i","o","u","A","E","I","O","U"] and j.isalpha():
        consonats+=1
    else:
        digits+=1


for i in b :
    for j in i :
        ul(j)
        vc(j)
print("Vowels: ",vowels)
print("Consonats: ",consonats)
print("Digits: ",digits)
print("Upercase: ",upercase)
print("Lowercase: ",lowercase)
f.close()
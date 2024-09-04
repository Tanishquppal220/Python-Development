def Upper(x):
    uc = 0
    for i in x:
        if i.isalpha() and i.isupper():
            uc += 1
    return uc


def Lower(x):
    lc = 0
    for i in x:
        if i.islower():
            lc += 1
    return lc


def Vowels(x):
    vo = 0
    for i in x:
        if i in "aeiouAEIOU":
            vo += 1
    return vo


def Consonants(x):
    co = 0
    for i in x:
        if i.isalpha() and i not in "aeiouAEIOU":
            co += 1
    return co


f = open(r"Report\\Text file.txt", "r+")
a = f.read()
f.close()
uc = Upper(a)
lc = Lower(a)
vo = Vowels(a)
co = Consonants(a)
print("Upper case letters:", uc)
print("Lower case letters:", lc)
print("Vowels:", vo)
print("Consonants:", co)
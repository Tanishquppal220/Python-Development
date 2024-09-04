def letter_freq(l):
    d = {}
    for i in l:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    return d
x = eval(input("Enter a list of string:"))
print(letter_freq(x))

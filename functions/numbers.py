'''
make a program input a list of number and  then increase odd mnumber by 1 and decrese even number of 1 and display in two diffrent list
'''
def odd(a):
    a += 1
    o.append(a)
def even(a):
    a -= 1
    o.append(a)

def opr():
    for i in n:
        if i % 2 == 0:
            even(i)
        else:
            odd(i)

o = []
e = []
n = eval(input('Enter a list of numbers'))
if type(n) == list:
    opr()
    print(o)
else:
    print("Enter a valid list")

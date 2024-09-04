def func2(d, c):
    for i in range(1, len(d)):
        if d[str(i)]["city"] == c:
            print(i, '.', d[str(i)]['Name'])


a = eval(input('Enter a dict of students :'))
b = input("Enter name of city:")
func2(a, b)


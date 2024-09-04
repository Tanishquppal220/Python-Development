'''def fuc1(x):
    l=[]
    for i in x:
        if i%2==0:
            l.append(i)
    l.reverse()
    print(l)
    print('Total no elenments in list is',len(l))
a=eval(input('Enter a list of numbers:'))
fuc1(a)
{'1':{"Name":"A","city":"Jalandhar"},'2':{"Name":"b","city":"amritsar"},'3':{"Name":"C","city":"Jalandhar"},'4':{"Name":"D","city":"amritar"}}
'''

def func2(d,c):
    for i in range(1,len(d)):
        if d[str(i)]["city"]==c:
            print(i,'.',d[str(i)]['Name'])

a=eval(input('Enter a dict of students :'))
b=input("Enter name of city:")
func2(a,b)

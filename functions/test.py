"""
name roll no and m arkis in {e,m,p,c,comp}
"""
n=int(input("Enter No of Student: "))
d={}

for i in range(n):
    n=input("Enter name of Student: ")
    r=int(input("Enter Roll no: "))
    e=int(input("Enter Marks in English: "))
    m=int(input("Enter Marks in Maths: "))
    p=int(input("Enter Marks in Physics: "))
    c=int(input("Enter Marks in Chemistry: "))
    comp=int(input("Enter Marks in Computer: "))
    total=p+m+c+e+comp
    pre=total/5
    marks={"English":e,'Physics':p, 'Maths':m,'Chemistry':c, 'Computer':comp,'Total':total, 'precentage':pre}
    d[r]={'Name':n, "marks":marks,}
    print()
print(d)






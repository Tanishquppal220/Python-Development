s="Racecar Car Radar"
l=s.split()
for w in l:
    x=w.upper()
    if x==x[::-1]:
        for i in x:
            print(i,end="*")
    else:
        for i in w :
            print(i,end="#")
    print()
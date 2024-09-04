r={"Pooja" : 70000, "Nidhi" :40000, "Bittu":80000, "Anu": 16000, "Anand":90000, "Vanita": 34000}
l=r.keys()
s=[]
for i in l:
    if r[i]>=50000:
        s.append(i)
print (s[::1])
print (s[::-1])
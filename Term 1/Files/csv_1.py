import csv
with open('csv_1.csv',"w+", newline='') as f:
    w=csv.writer(f)
    rec=[]
    # f.seek(2)
    while True:
        print("Enter students record:")
        rollno=int(input("Enter rollno:"))
        name=input("Enter name:")
        marks=int(input("Enter marks:"))
        data=[rollno,name,marks]
        rec.append(data)
        ans=input("Do you want to continue?(y/n)")
        if ans=='n':
            break
    for i in rec:
        w.writerow(i)
with open('csv_1.csv',"r+", newline='') as f:
    r=csv.reader(f)
    print(next(r))
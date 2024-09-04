import csv
def write_csv():
    n=int(input("Enter the number of employes: "))
    r=[]
    for i in range (n):
        name=input("Enter the name: ")
        age=int(input("Enter the age: "))
        salary=int(input("Enter the salary: "))
        r.append([name,age,salary])
    with open(r"table.csv","w+",newline='') as f:
        writer=csv.writer(f)
        writer.writerows(r)
def read_csv():
    s=input("enter a name:")
    with open("table.csv","r+") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[0]==s:
                print(row)
                break
            else:
                print("not found")  
# write_csv()
read_csv()
import json
def fun():
    r = int(input("Enter Roll Number Of Student: "))
    name = input("Enter Name Of Students: ")
    maths = int(input("Enter Marks Of Maths: "))
    physics = int(input("Enter Marks Of Physics: "))
    chemistry = int(input("Enter Marks Of Chemistry: "))
    english = int(input("Enter Marks Of English: "))
    computer = int(input("Enter Marks Of Computer: "))
    total = maths+physics+chemistry+english+computer
    prcentage = int((total/500)*100)
    marks = {'Maths': maths, 'Physics': physics, 'Chemistry': chemistry,
            'English': english, 'Computer': computer, "Total": total, "Percentage": prcentage}
    d[r] = {'Name': name, 'Marks': marks}
    print()
def display(x):
    print(json.dumps(d.get(x), indent=4), end="\n\n")
d={}
n = eval(input("Enter Total Number Of students: "))
for k in range(n):
    fun()
index = 0
while True:
    print("===============================================================================================================")
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4.Delete Student Details")
    print("5. Delete whole dictionary")
    print("6. Print Whole dict")
    print("7. Exit")
    index = int(input("Enter Your Choice: "))
    if index == 1:
        n = eval(input("Enter Number Of students To be Added: "))
        for k in range(n):
            fun()
    elif index == 2:
        c = int(input("Enter Roll Number Of Student: "))
        display(c)
    elif index == 3:
        Promoted = []
        for i in d:
            if d[i]['Marks']['Percentage'] >= 75:
                Promoted.append(d[i]['Name'])
        print(json.dumps(Promoted, indent=4), end="\n\n")
    elif index == 4:
        c = int(input("Enter Roll Number Of Student: "))
        confirm= input("Are You Sure You Want To Delete This Student Details (Y/N): ")
        if confirm == 'Y':
            d.pop(c)
            print("Student Details Deleted Successfully")
        else:
            continue
    elif index == 5:
        confirm = input("Are You Sure You Want To Delete Whole Dictionary (Y/N): ")
        if confirm == 'Y':
            d.clear()
            print("Dictionary Deleted Successfully")
        else:
            continue
    elif index == 6:
        print(json.dumps(d, indent=4), end="\n\n")
    else:
        print("Thank You")
        break

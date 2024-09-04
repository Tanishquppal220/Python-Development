import matplotlib.pyplot as plt
import json

test_inputs = [
    2,  # Total Number Of students
    1,  # Roll Number Of Students
    "Alice",  # Name Of Students
    90,  # Marks in Maths
    80,  # Marks in Physics
    85,  # Marks in Chemistry
    95,  # Marks in English
    100,  # Marks in Computer
    2,  # Roll Number Of Students
    "Bob",  # Name Of Students
    63,  # Marks in Maths
    60,  # Marks in Physics
    60,  # Marks in Chemistry
    60,  # Marks in English
    60,  # Marks in Computer
    7,
    'Physics',
    8,
    

]


def input(prompt=None):
    """Mock input function for testing."""
    if prompt:
        print(prompt, end="")
    test_input = str(test_inputs.pop(0))
    print(test_input)
    return test_input


def data(x):
    while x != 0:
        r = int(input("Enter Roll Number Of Students: "))
        name = input("Enter Name Of Students: ")
        maths = int(input("Enter Marks in Maths: "))
        physics = int(input("Enter Marks in Physics: "))
        chemistry = int(input("Enter Marks in Chemistry: "))
        english = int(input("Enter Marks in English: "))
        computer = int(input("Enter Marks in Computer: "))
        total = maths+physics+chemistry+english+computer
        prcentage = int((total/500)*100)
        marks = {'Maths': maths, 'Physics': physics, 'Chemistry': chemistry,
                 'English': english, 'Computer': computer, "Total": total, "Percentage": prcentage}
        d[r] = {'Name': name, 'Marks': marks}
        print()
        x -= 1


d = {}
n = eval(input("Enter Total Number Of students: "))
data(n)
index = 0
while index != 8:
    print("---------------------------------------------------------------------------------------------------------------")
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4. Delete Student Details")
    print("5. Print Whole dict")
    print("6. compare marks of students with graphs")
    print("7. marks of student in pie chart")
    print("8. Exit")
    index = int(input("Enter Your Choice: "))
    print()
    if index == 1:
        a = eval(input("Enter Total Number Of Entries you want to add: "))
        data(a)
    elif index == 2:
        c = int(input("Enter Roll Number Of Student: "))
        g = d[c]['Marks']
        print("Roll Number Of Student:", c)
        print("Name Of Student:", d[c]['Name'])
        print("Marks Of Student is:")
        for i in g:
            print("\t", end="")
            print("Marks Of ", i, "are", ":", g[i])
#         print("Total Marks Of Student is:", g['Total'])
#         print("Percentage Of Student is:", g['Percentage'])
    elif index == 3:
        g = {}
        l = []
        for i in d:
            g[d[i]['Name']] = d[i]['Marks']['Percentage']
        for j in g:
            if g[j] > 75:
                l.append(j)
        for i in l:
            a = i
            print(a)
    elif index == 4:
        c = int(input("Enter Roll Number Of Student: "))
        if c in d:
            confirm = input(
                "Are You Sure You Want To Delete This Student Details (Y/N): ")
            if confirm in ['Y', 'y']:
                print(json.dumps(d[c], indent=4), end="\n\n")
                d.pop(c)
                print("Deleted Successfully")
            else:
                continue
        else:
            print(c, "Not in The list")
    elif index == 5:
        print(json.dumps(d, indent=4), end="\n\n")
    elif index == 6:
        subject = input("Enter Subject Name: ")
        student_names = []
        student_marks = []

        for roll_no, student_details in d.items():
            student_names.append(student_details['Name'])
            student_marks.append(student_details['Marks'][subject])

        plt.bar(student_names, student_marks)
        plt.title(f'Comparison of {subject} marks')
        plt.xlabel('Student Name')
        plt.ylabel('Marks')
        plt.show()
    elif index == 7:
        subject = input("Enter Subject Name: ")
        student_names = []
        student_marks = []

        for roll_no, student_details in d.items():
            student_names.append(student_details['Name'])
            student_marks.append(student_details['Marks'][subject])

        plt.pie(student_marks, labels=student_names, autopct='%1.1f%%')
        plt.title(f'{subject} marks')
        plt.show()
    else:
        print("Thank You")
        break
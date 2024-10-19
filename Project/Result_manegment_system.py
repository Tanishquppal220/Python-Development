import json
import os
import sqlite3

# check if database.db is present or not
if not os.path.exists("Project/database.db"):
    # create database.db
    open("database.db", "w").close()

# connet to database.db
conn = sqlite3.connect("database.db")
# create cursor object
cur = conn.cursor()
# create table if table of name student is not present
cur.execute(
    """CREATE TABLE IF NOT EXISTS student(roll_no INTEGER PRIMARY KEY, name TEXT, maths INTEGER, physics INTEGER,
    chemistry INTEGER, english INTEGER, computer INTEGER, total INTEGER, percentage INTEGER)"""
)


def fun():
    """
    This Function Will Take Input From User And Store It Into Dictionary
    :return: None
    and store it into a list
    """
    n = eval(input("Enter Number Of students To be Added: "))
    for k in range(n):
        r = int(input("Enter Roll Number Of Student: "))
        name = input("Enter Name Of Students: ")
        maths = round(float(input("Enter Marks Of Maths: ")))
        physics = round(float(input("Enter Marks Of Physics: ")))
        chemistry = round(float(input("Enter Marks Of Chemistry: ")))
        english = round(float(input("Enter Marks Of English: ")))
        computer = round(float(input("Enter Marks Of Computer: ")))
        total = maths + physics + chemistry + english + computer
        percentage = round((total / 500) * 100)
        # STORE DATA INTO DATABASE
        cur.execute(
            f"INSERT INTO student VALUES({r}, '{name}', {maths}, {physics}, {chemistry}, {english}, {computer}, {total}, {percentage})")


def display(x):
    """
    This Function Will Take Roll Number As Input And Display The Details Of Student
    """
    k = cur.execute(f"SELECT * FROM student WHERE roll_no={x}")
    if k:
        print(json.dumps(k, indent=4), end="\n\n")
    else:
        print("Student Not Found")
    return 0


#  initialize index to 0
index = 0
# While loop for menu
while True:
    print(f'\n{"Welcome To Student Management System":^111}')
    print("=" * 111)
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4.Delete Student Details")
    print("5. Delete whole dictionary")
    print("6. Print Whole dict")
    print("7. Exit")
    index = int(input("Enter Your Choice: "))
    if index == 1:
        """
        This calls function fun() to take input from user and store it into database
        """
        fun()
    elif index == 2:
        c = int(input("Enter Roll Number Of Student: "))
        display(c)
    elif index == 3:
        Promoted = []
        # for i in d:
        #     if d[i]['Marks']['Percentage'] >= 75:
        #         Promoted.append(d[i]['Name'])
        for i in l:
            if i["Percentage"] >= 75:
                Promoted.append(i["Name"])
        print(json.dumps(Promoted, indent=4), end="\n\n")
    elif index == 4:
        c = int(input("Enter Roll Number Of Student: "))
        confirm = input("Are You Sure You Want To Delete This Student Details (Y/N): ")
        if confirm == "Y":
            d.pop(c)
            print("Student Details Deleted Successfully")
        else:
            continue
    elif index == 5:
        confirm = input("Are You Sure You Want To Delete Whole Dictionary (Y/N): ")
        if confirm == "Y":
            d.clear()
            print("Dictionary Deleted Successfully")
        else:
            continue
    elif index == 6:
        print(json.dumps(d, indent=4), end="\n\n")
    else:
        print("Thank You")
        break
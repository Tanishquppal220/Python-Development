import json
import os
import sqlite3

# check if database.db is present or not
if not os.path.exists("Project/database.db"):
    # create database.db
    os.system("touch Project/database.db")
# connect to database.db
conn = sqlite3.connect("Project/database.db")
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
        if list(cur.execute(f"SELECT * FROM student WHERE roll_no={r}")):
            print("Roll Number Already Exist")
            continue
        name = input("Enter Name Of Students: ")
        maths = round(float(input("Enter Marks Of Maths: ")))
        physics = round(float(input("Enter Marks Of Physics: ")))
        chemistry = round(float(input("Enter Marks Of Chemistry: ")))
        english = round(float(input("Enter Marks Of English: ")))
        computer = round(float(input("Enter Marks Of Computer: ")))
        total = maths + physics + chemistry + english + computer
        percentage = round((total / 500) * 100)
        cur.execute(
            f"INSERT INTO student VALUES({r}, '{name}', {maths}, {physics}, {chemistry}, {english}, {computer}, {total}, {percentage})")
        conn.commit()  # Commit the transaction

def display(x):
    """
    This Function Will Take Roll Number As Input And Display The Details Of Student
    """
    k = list(cur.execute(f"SELECT * FROM student WHERE roll_no={x}"))
    if not k:
        print("No Record Found!")
        return 0
    print(json.dumps(k, indent=4), end="\n\n")


#  initialize index to 0
def main():
    """
    This Function Will Display The Menu And Call The Function According To User's Choice
    """
    # make a list of all the roll numbers
    roll = list(cur.execute("SELECT roll_no FROM student"))
    print(f'\n{"Welcome To Student Management System":^111}')
    print("=" * 111)
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4. Delete Student Details")
    print("5. Delete All Records")
    print("6. Show Records Of All Students") 
    print("7. Exit")
    index = int(input("\nEnter Your Choice: "))
    print()
    if index == 1:
        """
        This calls function fun() to take input from user and store it into database
        """
        fun()
    elif index == 2:
        """
        1. Ask user to enter roll number of student
        2.calls function display() to display the details of student
        """
        c = int(input("Enter Roll Number Of Student: "))
        display(c)
    elif index == 3:
        """
        This gives the list of students who have more than 75% marks
        """
        Promoted = list(cur.execute("SELECT name FROM student WHERE percentage>75"))
        print(json.dumps(Promoted, indent=4), end="\n\n")
    elif index == 4:
        """
        1. Ask user to enter roll number of student
        2. Ask user to confirm the deletion
        3. if user confirms then delete the student details
        """
        c = int(input("Enter Roll Number Of Student: "))
        if confirm == "Y":
            confirm = input(f"Are You Sure You Want To Delete Record of Roll_no {c} (Y/N): ").upper()
            try:
                cur.execute(f"DELETE FROM student WHERE roll_no={c}")
                conn.commit()
                print("Student Record Deleted Successfully")
            except:
                print("No Record Found!")
    elif index == 5:
        confirm = input("Are You Sure You Want To Delete Record of every studnet (Y/N): ").upper()
        if confirm == "Y":
            cur.execute("DELETE FROM student")
            conn.commit()
            print("Records Deleted Successfully")
    elif index == 6:
        all_data = list(cur.execute("SELECT * FROM student"))
        print(json.dumps(all_data, indent=4), end="\n\n")
    else:
        print("Thank You")
        return 0
    return main()
main()
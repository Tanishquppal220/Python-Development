import mysql.connector as mysql
con = mysql.connect(host='localhost',user='root',password='tanishq',database='test')
if con.is_connected():
    cur = con.cursor()
    opt = 'y'
    # cur.execute("create table emp_1 (id integer primary key, name char(25),gender char(1),department char(10),salary integer)")
    while opt == 'y':
        id = int(input("Enter Employee ID:"))
        Name = input("Enter Employee Name:")
        Gender = input("Enter Employee Gender (M/F) :")
        Department = input("Enter Employee Department:")
        Salary = int(input("Enter Employee Salary:"))
        Query = "INSERT INTO emp_1 VALUES ({}, '{}' , '{}' , '{}' , {})".format(id, Name, Gender, Department, Salary)
        cur.execute(Query)
        con.commit()
        print("Record Stored Successfully")
        opt = input("Do you want to add another employee details (y/n) :")
    con.commit()
    con.close()
# //import mysql.connector as sql
# //con=sql.connect(host="localhost", user="root", password="tanishq",database="test")
# //cur=con.cursor()
# //cur.execute("select * from emp_1")
# //data=cur.fetchall()
# //print(data)

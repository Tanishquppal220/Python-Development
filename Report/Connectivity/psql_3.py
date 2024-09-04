import mysql.connector

con = mysql.connector.connect(
    host='localhost', user='root', password='root', database='test')

if con.is_connected():
    cur = con.cursor()
    print("Welcome to Employee Search Screen")
    No = int(input("Enter the employee number to search:"))
    Query = "SELECT * FROM emp_1 WHERE ID={}".format(No)
    cur.execute(Query)
    data = cur.fetchone()
    if data is not None:
        print(data)
    else:
        print("Record not Found !!!")
    con.close()

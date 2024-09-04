import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='root', database='test')

if con.is_connected():
    cur = con.cursor()
    print("Welcome to Employee Deletion Screen")
    No = int(input("Enter the employee number to delete:"))
    Query = "DELETE FROM emp_1 WHERE ID={}".format(No)
    cur.execute(Query)
    con.commit()
    print("Record Deleted Successfully")
    con.close()

import mysql.connector

con = mysql.connector.connect(
    host='localhost', user='root', password='root', database='test')

if con.is_connected():
    cur = con.cursor()
    print("Welcome to Employee Update Screen")
    No = int(input("Enter the employee number to update:"))
    field = input("Enter the field to update (Name/Department/Salary):")
    if field.lower() not in ['name', 'department', 'salary']:
        print("Invalid field")
    else:
        new_value = input(f"Enter new value for {field}:")
        if field.lower() == 'salary':
            new_value = int(new_value)
        Query = f"UPDATE emp_1 SET {field}='{new_value}' WHERE ID={No}"
        cur.execute(Query)
        con.commit()
        print("Record Updated Successfully")
    con.close()

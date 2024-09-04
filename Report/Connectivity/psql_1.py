import mysql.connector

# Predefined inputs
inputs = ["emp_1", "id", "INT", "name", "CHAR(25)", "gender", "CHAR(1)", "Dept", "char(25)", "salary", "INT", "id"]
input_iter = iter(inputs)

# Redefine input function


def input(prompt):
    value = next(input_iter)
    print(f"{prompt}{value}")
    return value


con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tanishq',
    database='test'
)

cur = con.cursor()

table_name = input("Enter table name: ")

fields = []
for i in range(1, 6):
    field_name = input(f"Enter name for field {i}: ")
    field_type = input(f"Enter type for field {i}: ")
    fields.append(f"{field_name} {field_type}")

primary_key = input("Enter the field name that should be the primary key: ")
fields.append(f"PRIMARY KEY ({primary_key})")

fields_str = ",\n".join(fields)

create_table_query = f"""
CREATE TABLE {table_name} (
    {fields_str}
)
"""

cur.execute(create_table_query)
print(f"Table {table_name} created successfully")

cur.close()
con.close()

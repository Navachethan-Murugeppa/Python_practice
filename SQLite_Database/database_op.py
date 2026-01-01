import sqlite3

conn = sqlite3.connect("Employee.db")

cursor = conn.cursor()
# create table
def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                      (first_name TEXT, last_name TEXT, Dept TEXT, salary INT)''')
    conn.commit()
create_table()

# Insert values in the table
def insert_employee(first_name, last_name, dept, salary):
    cursor.execute("INSERT INTO employees (first_name, last_name, Dept, salary) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, dept, salary))
    conn.commit()
# insert_employee("John", "Doe", "Python,Java", 70000)
# insert_employee("Jane", "Smith", "C++,JavaScript", 75000)
# insert_employee("Alice", "Johnson", "Go,Rust,Kubernetes", 80000)
# insert_employee("Michael", "Scott", "Management,Sales", 95000)
# insert_employee("Dwight", "Schrute", "Sales,Beets", 60000)

# read values from the table

def fetch_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Name: {row[0]} {row[1]}, Dept: {row[2]}, Salary: ${row[3]}")
fetch_employees()
print( " ")


def fetch_specific_employee(first_name):
    cursor.execute("SELECT * FROM employees WHERE first_name=?", (first_name,))
    row = cursor.fetchone()
    if row:
        print(f"Name: {row[0]} {row[1]}, Dept: {row[2]}, Salary: ${row[3]}")
    else:
        print(f"No employee found with the first name {first_name}")
print("\nFetching specific employee:")
fetch_specific_employee("Alice")

#Update values
def update_employee_salary(first_name, new_salary):
    cursor.execute("UPDATE employees SET salary=? WHERE first_name=?", (new_salary, first_name))
    conn.commit()
    print(f"Updated salary for {first_name} to ${new_salary}")
    
update_employee_salary("Dwight", 65000)

conn.close()



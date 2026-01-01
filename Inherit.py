class Employee:
    inc_amt = 1.05
    def __init__(self, first_name, last_name, salary, dept):
        print("Initializing Employee...")
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.dept = dept
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
    
    def full_name(self):
        # return f"{self.first_name} {self.last_name}"
        return "{} {}".format(self.first_name, self.last_name)
    
    def display_details(self):
        print("Class {}".format(type(self).__name__))
        print("\nEmployee Details:")
        print(f"Name: {self.full_name()}")
        print(f"Email: {self.email}")
        print(f"Department: {self.dept}")
        print(f"Salary: ${self.salary}\n")
    
    def update_department(self, new_dept):
        self.dept = new_dept
        print(f"Department updated to {self.dept} for {self.full_name()}")
    
    def inc_salary(self):
        self.salary += self.salary * self.inc_amt
        print(f"New salary is ${self.salary}")

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, dept, emp_count):
        print("Initializing Manager...")
        super().__init__(first_name, last_name, salary, dept)
        self.emp_count = emp_count
    def display_details(self):
        super().display_details()
        print(f"Manages {self.emp_count} employees.\n")
    
    def inc_emp_count(self, count):
        self.emp_count += count
        print(f"Employee count updated to {self.emp_count} for Manager {self.full_name()}")
    

emp2 = Employee("Jane", "Smith", 75000, ["C++", "JavaScript"])
emp3 = Employee("Alice", "Johnson", 80000, ["Go", "Rust", "Kubernetes"])

mgr1 = Manager("Michael", "Scott", 95000, ["Management", "Sales"],25)
mgr1.display_details()


emp2.display_details()
emp3.display_details()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}, Salary: ${self.salary:,.2f}"

class Manager(Employee):
    def long_term_bonus(self):
        return self.salary * 0.40  

    def display_info(self):
        return f"Manager: {self.name}, Salary: ${self.salary:,.2f}, Long-term Bonus: ${self.long_term_bonus():,.2f}"

class Executive(Manager):
    def executive_bonus(self):
        return self.salary * 2.00  

    def long_term_bonus(self):  
        return self.salary * 0.50  

    def display_info(self):
        return f"Executive: {self.name}, Salary: ${self.salary:,.2f}, Long-term Bonus: ${self.long_term_bonus():,.2f}, Executive Bonus: ${self.executive_bonus():,.2f}"

manager1 = Manager("Alice Johnson", 80000)
print(manager1.display_info())

executive1 = Executive("Bob Williams", 120000)
print(executive1.display_info())

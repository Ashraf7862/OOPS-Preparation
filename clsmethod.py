class Employee:
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        return f"Company: {Employee.company}\nName: {self.name}\nSalary: {self.salary}"   #we can also use <self.company>

    @classmethod
    def change_company(cls):
        cls.company="Microsoft"

emp1=Employee("aaa",20000)
emp2=Employee("aba",40000)
emp3=Employee("acc",50000)
print(emp1.display())
print(emp2.display())
print(emp3.display())
Employee.change_company()
print()
print(emp1.display())
print(emp2.display())
print(emp3.display())
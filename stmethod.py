class Employee:
    @staticmethod
    def is_valid_salary(salary):
        if salary>0:
            return True
        return False

object=Employee()
print(object.is_valid_salary(0))
print(object.is_valid_salary(1000))
print(Employee.is_valid_salary(5000))
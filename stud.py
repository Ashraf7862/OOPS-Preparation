class disp:
    def __init__(self,data):
        self.name=data.name
        print(self.name)

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        return f"Name: {self.name}\nAge: {self.age}\nMarks: {self.marks}"

if __name__=="__main__":
    object1=Student("rahul",18,98)
    object2=Student("Arun",19,99)
    print(object1.name)
    print(object1.age)
    print(object2.name)
    disp(object1)

    print(object1.display())
    print()
    print(object2.display())

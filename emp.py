class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class fullEmp(Employee):
    def __init__(self,name,id,sal):
        super().__init__(name,id)
        self.sal=sal

    def salary(self):
        print(self.sal)

class partEmp(Employee):
    def __init__(self,name,id,hsal,hrs):
        super().__init__(name,id)
        self.sal=hsal
        self.hrs=hrs
        self.total_sal=hsal*hrs

    def salary(self):
        print(self.total_sal)

f=fullEmp("rahul",1,1000)
f.salary()
t=partEmp("arun",2,250,10)
t.salary()




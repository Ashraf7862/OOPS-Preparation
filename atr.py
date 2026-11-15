class Student:
    school="ABC SCHOOL"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    

s1=Student("Arun",19)
s2=Student("Rahul",20)
s1.school="DEF"
print(s1.school)
del s1.school
print(s1.school)
print(s2.school)
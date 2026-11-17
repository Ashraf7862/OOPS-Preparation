class Student:
    def __init__(self,marks):
        self.__marks=marks

    @property
    def mark(self):
        return self.__marks

    @mark.setter
    def mark(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks")

student=Student(85)

print(student.mark)

student.mark=95
print(student.mark)

student.mark=150
print(student.mark)
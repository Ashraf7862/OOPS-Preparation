#The main purpose: Every child class must provide its own implementation of the abstract method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self,length,width):
        return length*width


object=Rectangle()
print(object.area(10,5))
# Method overriding

print("# Method overriding\n")
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

car=Car()
bike=Bike()
vehicle=Vehicle()

car.start()
bike.start()
vehicle.start()
print()


# Duck Typing

print("# Duck Typing\n")
class Duck:
    def quack(self):
        print("Duck is quacking")

class Person:
    def quack(self):
        print("Person is imitating a duck")

class Robot:
    def quack(self):
        print("Robot is making a quack sound")

def make_quack(obj):
    obj.quack()

duck=Duck()
person=Person()
robot=Robot()

make_quack(duck)
make_quack(person)
make_quack(robot)
print()


# Method Overloading

print("# Method Overloading\n")
# Does Python support method overloading? 
# Not in the traditional way.

class Calculator:
    def multiply(self,*args):
        ans=1
        for i in args:
            ans*=i
        print(ans)

obj=Calculator()
obj.multiply(2, 3)
obj.multiply(2, 3, 4)
obj.multiply(2, 3, 4, 5)
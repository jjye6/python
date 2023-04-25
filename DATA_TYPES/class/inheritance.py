# Allows you to create a hierarchy of classes that share a set of properties and methods
# by deriving a class from another class.

class Person():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

# Inherited or subclass
class Employee(Person):
    def isEmployee(self): # changes
        return True

emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
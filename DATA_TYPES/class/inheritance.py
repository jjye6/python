# Allows you to create a hierarchy of classes that share a set of properties and methods_class by deriving a class from another class.

class Person():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def employee(self):
        return False

# Inherited or subclass
class Employee(Person):
    def employee(self): # changes
        return True

ex = Person("Carlos")
print(ex.get_name(), ex.employee()) # Carlos False

ex = Employee("Roberto")
print(ex.get_name(), ex.employee()) # Roberto True
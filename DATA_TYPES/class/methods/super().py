# Returns objects represented in the parent’s class
# If both classes have init method, an error will rise

class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Child(Person):
    def __init__(self, id, name, email):
        super().__init__(id, name) # inhertis the variables
        self.email = email

e = Child(10, "marc", "KKK@gmail.com")

print('The ID is:', e.id) # The ID is 10
print('The name is:', e.name) # The name is marc
print('The email is:', e.email) # The email is KKK@gmail.com
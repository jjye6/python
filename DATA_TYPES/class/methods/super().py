# Returns objects represented in the parent’s class
# If both classes have init method, an error will rise

class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Child(Person):
    def __init__(self, id, name, email):
        super().__init__(id, name)
        self.email = email

e = Child(10, "marc", "KKK@gmails")
print('The ID is:', e.id)
print('The Name is:', e.name)
print('The Emails is:', e.email)
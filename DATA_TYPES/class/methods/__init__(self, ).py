# Initializes the object’s state (requires parameters)

class Person:
    def __init__(self, name): # methods or constructor
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


m = Person("Marc")
p = Person("Pedro")

print(m.name)
print(p.name)

m.say_hi()
p.say_hi()
# Initializes the object’s state (requires parameters)

class Person:
    def __init__(self, name): # methods_class or constructor
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


m = Person("Marc")
p = Person("Pedro")

print(m.name) # Marc
print(p.name) # Pedor

m.say_hi() # Hello, my name is Marc
p.say_hi() # Hello, my name is Pedro
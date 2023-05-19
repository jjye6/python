class Dog:
    ex = "mammal"

    def fun(self):
        print("I'm a", self.ex)

d = Dog() # instance

d.fun() # I'm a mammal
print(d.ex) # mammal

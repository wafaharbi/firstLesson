# _______________ 42 Day _______________ #

# Python Classes and objects 2

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def fun(self):
        print("Hello my name is " + self.name)

p1 = Person("Wafa", 25)
p1.fun()


class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def fun(self):
        print("Hello my name is " + self.name)

p1 = Person("Wafa", 25)
p1.age = 24

print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def fun(self):
        print("Hello my name is " + self.name)

p1 = Person("Wafa", 25)
del p1.age

#print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def fun(self):
        print("Hello my name is " + self.name)

p1 = Person("Wafa", 25)
del p1

#print(p1)


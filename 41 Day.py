# _____________________ 41 Day _____________________ #

#Python Calsses and Objects

class Myclass:
    x = 5
print(Myclass)


class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)


class Person:
 def __init__(self , name, age):
     self.name = name
     self.age = age

p1 = Person("wafa", 25)
print(p1.name)
print(p1.age)



class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def fun(abc):
        print("Hello my name is " + abc.name)

p1 = Person("wafa" , 25)
p1.fun()

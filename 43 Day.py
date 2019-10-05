# ____________ 43 Day _____________ #

# Python inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname= fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("wafa", "alharbi")
x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname= fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("aisha" , "alharbi")
x.printname()



class Person:
    def __init__(self, fname, lname):
        self.firstname= fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname , lname):
        Person. __init__(self,fname,lname)

x = Student("wafa", "alharbi")
x.printname()
        

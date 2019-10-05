# ______________ 44 Day ________________ #

# Python inheritance2


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)


x = Student("wafa","abdulaziz")
x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)
        self.graduationyear = 2018

x = Student("wafa","abdulaziz")
print(x.graduationyear)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

x = Student("wafa","abdulaziz", 2018)
print(x.graduationyear)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year
    def welcome(self):
        print("welcome" , self.firstname, self.lastname,"to class of ",self.graduationyear)
        
x = Student("wafa","alharbi", 2018)
x.welcome()

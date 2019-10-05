# ____________ 45 Day ____________ #

#Python Iterators

mytuble = ("apple", "banana", "cherry")
myit = iter(mytuble)

print(next(myit))
print(next(myit))
print(next(myit))



mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


mytuble = ("apple", "banana", "cherry")

for x in mytuble:
    print(x)


mystr = "banana"
for x in mystr:
    print(x)


class numbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
myclass = numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class numbers:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass = numbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
  

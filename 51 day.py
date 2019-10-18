# _______________ 51 Day ________________ #

#Python Modules 2

import mymodule as mx

a = mx.person1["age"]
print(a)


import platform

x = platform.system()
print(x)

import platform
print(platform.python_version())


import platform
x = dir(platform)
print(x)


def greeting(name):
    print("Hello, ",  name)

person1 = {
    "name": "Jhon",
    "age": 25,
    "country": "Norway"
    }

from mymodule import person1
print(person1["age"])

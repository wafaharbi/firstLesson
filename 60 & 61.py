# ___________ Day 60 & 61 _______________ #


# First Challenge

import json
import re

DaysOfWeeks = ("Sunday", "Monday", "Tuesday","Wednesday","Thirsday","Friday")
print(type(DaysOfWeeks))

myJson = json.dumps(DaysOfWeeks)
print(myJson)
print("\n")

# Second Challenge

str = "data is the new oil"
x = re.findall("data", str)
print("Search is: ", x)

# additional Challenge


python = {
    "language name": "Python",
    "Defination": "Python is an interpreted, high-level, general-purpose",
    "created by": "Guido van Rossum",
    "Data created": "first released in 1991",
    }

print(json.dumps(python, indent=4))

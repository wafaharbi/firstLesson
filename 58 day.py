# _______________ 58 day ___________ #

#Python RegEx2

import re

str = "The rain in Spain"
x = re.findall("ai",str)
print(x)

str = "The rain in Spain"
x = re.findall("pol",str)
print(x)

if (x):
    print("Yes, there is at least one match")
else:
    print("No match")


str = "The rain in Spain"
x = re.search("\s",str)
print("the first white-space charecter is located in position: ",x.start())

str = "The rain in Spain"
x = re.search("pol",str)
print(x)


str = "The rain in Spain"
x = re.split("\s",str)
print(x)

# ____________ 59 Day ____________#

#Python RegExp3

import re

str = "The rain in Spain"
x = re.sub("\s","9",str)
print(x)

str = "The rain in Spain"
x = re.sub("\s","9",str, 2)
print(x)

str = "The rain in Spain"
x = re.search("ai",str)
print(x)

str = "The rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.span())


str = "The rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.string)


str = "The rain in Spain"
x = re.search(r"\bS\w+",str)
print(x.group())

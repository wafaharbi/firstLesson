# __________________ Ninth Day ____________________ #

"""To combine String and numbers
Use the format() method to insert numbers into strings"""

age = 24
txt = "My name is wafa, I am "

print(txt.format(age), "\n")

# The format() method takes unlimited number of arguments

quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."

# Will print " I want 3 pieces of item 567 for 49.95 dollars."
print(myorder.format(quantity, itemno, price), "\n")


quantity = 3
itemno = 567
price = 49.95

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

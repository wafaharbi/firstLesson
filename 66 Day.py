# ________________ 66 Day ________________ #

#Python String Formatting 2

quantity = 3
itemNo = 567
price = 49
myOrder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myOrder.format(quantity, itemNo, price))



age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#Named Indexes

myOrder = "I have a {carname}, its a {model}."
print(myOrder.format(carname = "Ford", model = "Mustang"))

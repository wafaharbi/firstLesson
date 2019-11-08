# ___________ 65 day ________________ #

#Python String Formatting

price = 49
txt = "The price is {} dollrs"

print(txt.format(price))


# Multiple Values

quantity = 3
itemNo = 567
price = 49
myOrder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myOrder.format(quantity, itemNo, price))

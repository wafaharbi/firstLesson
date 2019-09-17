# ______________ 29 Day _________________ #

# Python loops2

fruits = ["apple", "banana","orange"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)


# break statement

fruits = ["apple", "banana","orange"]
for x in fruits:
    print(x)

    if x == "banana":
        break


fruits = ["apple", "banana","orange"]
for x in fruits:
    print(x)

    if x == "banana":
        break
    print(x)
    
# continue statement
fruits = ["apple", "banana","orange"]
for x in fruits:
    if x == "banana":
      continue
    print(x)
    

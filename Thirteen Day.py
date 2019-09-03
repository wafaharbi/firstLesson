# ____________________ Thirteenth _____________________ #

# The lists in Python are wirtten with [ ]

s = []
print(s)

numbers = [1,2,3,4,5]
print(numbers)


lists =["apple","banan","cherry"]
print(lists)

thelist = ["apple","banana","cherry",1,2,3]
print(thelist)
print("\n")


# access the list items by referring to the index number

lists =["apple","banan","cherry"]
print(lists[1])
print("\n")

# Using for loop

lists =["apple","banan","cherry"]
print("using for loop :")
for x in lists:
    print(x)
    


print("\n","change the second wird in the lisis:")
lists =["apple","banan","cherry"]

lists[1]="orange"
print(lists)


# delete the first word in the lists
lists =["apple","banan","cherry"]
del lists[0]
print(lists)

# delete the all word in the lists
lists =["apple","banan","cherry"]
# del lists will delete the lists

lists = ["A","B","C","D","E"]
print(lists)

del lists[0]
del lists[1]

print(lists)



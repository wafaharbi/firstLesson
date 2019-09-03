# ___________________ Fifteenth Day _____________________ #

# Python List3

# The list use len() methods

lists = ["wafa","daliah","redana"]
print("The length if list name is: ",len(lists))

# Using append() methods
lists = ["wafa","daliah","redana"]
print("\n", " appends of amjed")
lists.append("amjad")

print(lists)


# Using insert() methods

lists = ["wafa","daliah","redana"]
lists.insert(1,"Noura")
print("\n"," insert Noura in a list")
print(lists)


# Using remove() methods

lists = ["wafa","daliah","redana"]
lists.remove("wafa")
print("Remove wafa from the list: ",lists)

# Using pop() methods

lists = ["wafa","daliah","redana"]
lists.pop()
print(lists)

# Using clear() methods
lists = ["wafa","daliah","redana"]
lists.clear()
print(lists)

# Using copy() methods
lists = ["wafa","daliah","redana"]
listName = lists.copy()
print(listName)

# equalize to lists
lists = ["wafa","daliah","redana"]
listName = lists
lists.pop(0)
print(listName)
print(lists)

# Using list() methods
lists = ["wafa","daliah","redana"]
listName = list(lists)
print(listName)

thislist = list(("wafa","daliah","redana"))
print(thislist)

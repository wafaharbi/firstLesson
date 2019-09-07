# _______________ Week 3 Challenges _________________ #
# _______________ Day 18 & 19 ___________________ #

# Write a list then use 4 methods on it

ListName = ["wafa","noura","aisha","afnan","jouharah"]
print("The list is :")
print(ListName,"\n")


# use append() function to add member in list
ListName.append("amnah")
print("add amnah to list name")
print(ListName,"\n")


# use remove() function to remove an elements in list
ListName.remove("amnah")
print("the list after removing 'amnah'")
print(ListName)

# user copy() function to copy list to another list
Lists = ["ahmed","mohammed","omar","sami"]
ListName = Lists.copy()
print("copy list name1 to other list:")
print(ListName,"\n")


# use sort() function to sort the list
ListName.sort()
print(" list after sorting :")
print(ListName,"\n")

# ____________ using Tuple ____________ #

tuple = ("java","python","swift")
print("the elemnts of tuple are")
print(tuple)
if "java" in tuple:
    print("yes , (java) is in tuple")

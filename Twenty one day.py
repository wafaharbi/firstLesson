# ____________________ twenty one day _________________ #

sets = {"java","python","swift"}

#use len() function 
print(len(sets))

# use remove() function to remove element in sets
sets.remove("java")
print(sets,"\n")

#use discard() function to remove element in sets
sets = {"java","python","swift"}
sets.discard("swift")
print(sets,"\n")

# use pop() method to return element that removing
sets = {"java","python","swift"}
x = sets.pop()
print(x)
print(sets)

# use clea() method to clear the sets
sets = {"java","python","swift"}
sets.clear()
print(sets)


# use del() methods to delete set completely
sets = {"java","python","swift"}
##del sets
##print(sets)


# use set() constructor to make a set
sets = set(("java","python","swift"))
print(sets)


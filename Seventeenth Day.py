# ___________________ Seventeenth Day _______________ #

# Python Tuples2

# using 'in' in tuples

Tuple = ("wafa","emaan","noura")
if "wafa" in Tuple:
    print("Yes. 'wafa' is in name tuple")
    
# using '*' operator in tuples
Tuple = ("Python",) * 3
print(Tuple)

#Using 2 tuples 
tuple1 = (1, 2, 3, 4)
tuple2 = (5 ,6)
tuple3 = tuple1 + tuple2
print(tuple3)

x = (3,4,5,6)
x = x + (7,8,9)
print(x)

#Using len() method
Tuple = ("wafa","emaan","noura")
print(len(Tuple))


# Tuple() consructor
Tuple = tuple(("wafa","emaan","noura"))
print(Tuple)

Tuple = [3,4,5,6,"A","B"]
Tuple = tuple(Tuple)
print(Tuple)


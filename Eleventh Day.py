# ________________ Eleventh Day ____________________ #


# The Logical Operator in Python

x = 5
print("   The Logical Operators or ,ond , not   ")
print(" 5 is greater then 3 OR 5 is less then 4 : ", x > 3 or x < 4 , "\n")
print(" 5 is greater then 3 AND 5 is less then 4 : ", x > 3 and x < 4 , "\n")
print(" 5 is greater then 3 NOT 5 is less then 4 : ",not( x > 3 and x < 4) , "\n")


"""Is operator returens true if both variables are the same object
 Is not operator returens true if both variables are not the same object
"""

x = ["apple","orange"]
y = ["apple","orange"]

z = x

print("Is x same of z ? ",x is not z, "\n")    # return false
print("Is x same of y ? ",x is not y, "\n")    # return true
print("Is x same of y ? ",x != y, "\n")        # return false

""" in operator return true if a sequence with value is present in the object
and not in return true if a sequence with the value is not present in the object
"""

x = ["apple","orange"]

#This will return true 
print("Is orange value is present in object ? " , "orange" in x ,"\n")

y = ["tea" , "juice"]

#This will return flase
print("Is orange value is present in object ? " , "orange" in y ,"\n")

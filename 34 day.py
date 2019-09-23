# ____________________ 34 Day _____________________ #

#Python Function 2

#passing a parametr

def functions(food):
    for x in food:
        print(x)


fruits = ["apple","banana","cherry"]
functions(fruits)


# return a value
print("\n","The return value is an integer:")

def functions(x):
    return 5 * x

print(functions(2))
print(functions(5))
print(functions(10))


#Keyword Arguments
print("\n")

def functions(child3, child2, child1):
    print("The youngest child is" + child3)

functions(child1 = "Email", child2 = "Tobias", child3 = "Linus")

#Arbitray Arguments
print("\n")

def functions(*kids):
    print("The youngest child is" + kids[2])

functions("Email","Tobias","Linus")


#Recursion

def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n \n Recursion function result :")
tri_recursion(6)

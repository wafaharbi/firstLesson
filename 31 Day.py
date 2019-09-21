# ____________________ 31 Day ______________________ #

# Python Functions

# use def to define a function

def functions() :
    print(" this is a function ")


# calling a functoin

print("calling a function:")
functions()

# define a parameter in function

def functions(name) :
    print(name,"refrence")

functions("Email")

# default parameter
def functions(country = "riyadh") :
    print("I am from " + country)
functions()
functions("Sauia")

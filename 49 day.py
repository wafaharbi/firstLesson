# ___________ 49 Day ____________ #

#Python scope2

#Naming Variables

x = 300      # global variable
def fun():
    x = 300    # local variable
    print(x)

fun()

print(x)

def fun():
    global x
    x = 300

fun()

print(x)


x = 300

def fun():
    global x
    x = 200

fun()
print(x)

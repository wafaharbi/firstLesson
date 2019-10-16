# ______________ 48 Day ________________ #


#Python Scope

# local scope

def fun():
    x = 300
    print(x)


fun()


def fun():
    x = 300
    def innerFun():
        print(x)
    innerFun()

fun()

#Global Scope

x = 300
def fun():
    print(x)

fun()
print(x)

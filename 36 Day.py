# _________________ 36 Day ___________________ #

#Python Lambda2

def fun(n):
    return lambda a : a * n

x = fun(2)
print(x(11))


def fun(n):
    return lambda a : a * n

x = fun(3)
print(x(11))



def fun(n):
    return lambda a : a * n


x = fun(2)
y = fun(3)

print(x(10))
print(y(10))

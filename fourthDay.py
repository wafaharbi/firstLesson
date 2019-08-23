# The Numeric Variables in Python are created when assigning value to it

# assign an integer number to variable x
x = 4
print("x is an integer number ", x)


# assign a float number to variable y
y = 2.5
print("y is a float number " , y)

# assign a complix number to variable z
z = 1j
print("z is a comlex number " , z , "\n")



# Using the type() Function to varify the type of object

print(type(x))     #integer

print(type(y))     #float

print(type(z))     #complex

print("\n")   #print new line

# The integer numbers are positive or negative without decimals

integer = 1     #integer

PositiveInt = 34566660979   # positive integer number

NegativeInt = -563267       # negative integer number

print(type(integer))        #integer type
print(type(PositiveInt))    #integer type
print(type(NegativeInt))    #integer type

print("\n")     #print new line

"""
# The Float numbers are positive or negative with decimals,
and  also indicate the power of 10 """

floatNum = 1.12         # float number
PaositiveFloat = 4.5    # Positive floar number
NegativeFloat = - 15.6  #Negative float number


print(type(floatNum))         #float type
print(type(PaositiveFloat))   #float type
print(type(NegativeFloat))    #float type

print("\n")     #print new line

xPower = 2e3   
yPower = 12E2
zPower = -8.2e10

print(type(xPower))       #float type
print(type(yPower))       #float type
print(type(zPower))       #float type

print("\n")     #print new line


# The complex number are written with j or J
xcomplex = 3+2j          #complex number
yComplex = 5j            #positive complex number
zComplex = -5j           #Negative complex number

print(type(xcomplex))       #complex type
print(type(yComplex))       #complex type
print(type(zComplex))       #complex type

print("\n")     #print new line



# Using int() , float() and complex() methods to convert one type to another

xInt = 2          # int number
yFloat = 1.5      # float number
zComplex = 4j     # complex number

a = float(xInt)     # Convert from int to flaot
b = int(yFloat)     # Convert from float to int
c = complex(xInt)  #Convert from int to complex

print("conver 2 to float number = ", a)
print("convert 2.5 to int number = ", b)
print("convert 2 to complex number = " , c)

print("\n")     #print new line

print(type(a))  #float number
print(type(b))  #integer number
print(type(c))  #complex number

#Using random number

import random
print("\n")     #print new line
print(random.randrange(1,10))  #print random number in range from 1 to 10


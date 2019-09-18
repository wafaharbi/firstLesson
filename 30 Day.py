# _________________  thertiy Day ____________ #

# Python Loops3
# Using for loop

# range()
print("range from 0 to 6")
for x in range(6):
    print(x)

    
print("rage from 2 to 6")    

for x in range(2,6):
    print(x)
    
print("rage in between 2 ,30 , 3")    

for x in range(2,30,3):
    print(x)

# use else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished")


#Nasetd Loop

name = ["wafa","sara","noura"]
adj = ["good","better","nice"]

for x in name:
    for y in adj:
        print(x,y)

# __________________ 39 and 40 _______________ #


# Qestion1

def power_number(num, power):
    if power > 0:
        result = num * power_number(num, power-1)
    else:
         result = 1
    return result


print("The result of 5 power 3 = ", power_number(5, 3),"\n")


# Qestion2

numberList = [-4, -6, -5 , -1, 2, 3, 7, 9, 88]
print(numberList)
positiveNum = []

isPositive = lambda num : num > 0

for num in numberList:
    if (isPositive(num)):
        positiveNum.append(num)

print(positiveNum)

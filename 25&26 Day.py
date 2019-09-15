 # ____________________ 25 & 26 Day _____________________ #

 
# adding number 4,8,12 to the set {1,3,5,7,8}

setNum = {1,3,5,7,8}
setNum.update([4,8,12])
print(setNum)


# delete 8 from set
setNum.remove(8)
print(setNum)

# set is empty
setNum.clear()
print(setNum)


# create a dictionary

dictionary ={"name": "brid",
             "skin cover" : "features"}
print(dictionary)


#add type() function
t = type(dictionary)
print(t)

#change "skin cover" item in dictionary
dictionary["skin cover"] = "skin"
print(dictionary)

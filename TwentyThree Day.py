# ____________ Twenty Three Day _____________ #

# Python Dictionary 2

dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
if "model" in dictionary:
    print("yes, 'model' is one of the keys in the dictionary")

# dictionary len()

dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
print(len(dictionary))


# adding a new index in dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
dictionary["color"] = "red"
print(dictionary)

# removing item in the dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
dictionary.pop("model")
print(dictionary)

# use popitem() function to remove last item in dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
dictionary.popitem()
print(dictionary)

# use del() fuction to delete item on the dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
del dictionary["model"]
print(dictionary)

# use del() fuction to delete all dictionary
##dictionary = {
##    "brand": "Ford",
##    "model": "Mustang",
##    "year": 1964
##    }
##del dictionary
##print(dictionary)

# use clear() fuction to remove all item in the dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
dictionary.clear()
print(dictionary)

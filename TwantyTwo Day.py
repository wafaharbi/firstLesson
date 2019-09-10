# _______________ Twenty Two Day __________________ #


# Python Dictionries
dictionary = {}
print(dictionary)


dictionary = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
    }
print(dictionary,"\n")

dictionary = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
    }
x = dictionary["model"]
print(x)

dictionary = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964
    }
x = dictionary.get("model")
print(x,"\n")

#change the year to 2018
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
dictionary["year"] = 2018



# using loop in a dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in dictionary:
    print(x)

print("\n")
# To print all elemnt in the dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in dictionary:
    print(dictionary[x])

print("\n")

# use values() function
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in dictionary.values():
    print(x)

print("\n")

# use items() function
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x,y in dictionary.items():
    print(x,y)

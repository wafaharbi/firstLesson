# ______________ Twenty Four Day _______________ #

# Python dictionary 3

dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
myDict = dictionary.copy()
print(myDict)


dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

myDict = dict(dictionary)
print(myDict)

Family = {
    "chiald1" : {
        "name" : "Email",
        "year" : 2004
        },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
        },
    "child3" : {
       "name" : "Linus",
        "year" : 2011
       }
    }
print(Family)

child1 = {
        "name" : "Email",
        "year" : 2004
        }
child2 =  {
        "name" : "Tobias",
        "year" : 2007
        }
child3 =  {
       "name" : "Linus",
        "year" : 2011
       }
Family = {
          "child1" : child1,
          "child2" : child2,
          "child3" : child3
          }
print(Family)

#The dict() Constructor
dictionary = dict(brand = "Ford" , model = "Mustang" , year = 1964)
print(dictionary)


      

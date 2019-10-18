# _____________ 55 day ____________#

# Pyhton JSON

import json

x = '{ "name":"wafa", "age":24, "city":"Qassim"}'
y = json.loads(x)
print(y["age"])


# convert from python to json

x = {
    "name":"wafa",
    "age":24,
    "city":"Qassim"
    }

y = json.dumps(x)

print(y)


import json

print(json.dumps({
    "name":"wafa",
    "age":24,
    "city":"Qassim"
    }))
print(json.dumps(["apple", "banana"]))

print(json.dumps(("apple", "banana")))
print(json.dumps(("Hi")))
print(json.dumps((24)))
print(json.dumps((30.75)))
print(json.dumps((True)))
print(json.dumps((False)))
print(json.dumps((None)))

# _______________ 56 day ____________ #

#Python JSON 2

import json

x = {
    "name":"wafa",
    "age":24,
    "married":False,
    "discoverd":False,
    "children":None,
    "pets":None,
    "cars": [
        {"model": "BMW 230","mpg":27.5},
        {"model": "Ford edge","mpg":24.1}
        ]
    }

print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4, separators=(". "," = ")))

print(json.dumps(x, indent = 4 , sort_keys=True))


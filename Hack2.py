import json

expirations = {"BEEF": 4,
               "CHICKEN": 4,
               "PORK": 4,
               "CABBAGE": 30,
               "CORN": 4,
               "CUCUMBER": 10,
               "EGGPLANT": 11,
               "SPINACH": 11,
               "MUSHROOM": 7,
               "TOMATO": 5,
               "AVOCADO": 10,
               "POTATO": 60,
               "CARROT": 45,
               "ONION": 60,
               "SHELLFISH": 1,
               "FISH": 1}

data = '{"foodtype": "meat", "type": "beef", "date": "09.24.2022", "quantity": 5}'

retrieve = json.loads(data)

# store data

retrieve["expdate"] = expirations[retrieve["type"].upper()]
print(retrieve)


# export = json.dumps()

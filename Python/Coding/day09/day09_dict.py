person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    # "stats": {"goals": 300, "assists": 500},
    "sport": "football",
    # "height": 168,
}

# print(person["stats"]["goals"]) # KeyError: 'stats'
# print(person.get("stats").get("goals")) # 'NoneType' object has no attribute 'get'

# Default value - person.get(key, default value)
print(person.get("height", 174))
print(person.get("stats", {}).get("goals"))  # None
print(person.get("stats", {"goals": 0}).get("goals"))  # None

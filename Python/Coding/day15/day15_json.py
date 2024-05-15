import json

data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
    ]
}


print(type(data))  # dict
# Dict -> JSON

data_json = json.dumps(data, indent=4)
print(data_json)
print(type(data_json))  # string

print(data["employees"])
print(data["employees"][0])
# print(data_json["employees"]]) # error ❌


def dbl(x):
    return x * 2


sport = {"name": "Dhoni", "dbl": lambda x: x * 2}

print(dbl(4))
print(sport["dbl"](4))
print(sport["dbl"])
print(sport["name"])
print(type(sport))

# sport_json = json.dumps(sport) # ❌ not JSON serializable


student_json = """
{
    "name": "Tonika",
    "gender": "female"
}
 
"""

student = json.loads(student_json)  # convert to dict
print(type(student))
print(student)
print(student["name"])

# json.dumps  -> dumps as JSON
# json.loads  -> loads into dict


bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""


# Task 1 (normal for loop)
# All Active user's balance should increase by 10%
# Final Output should be JSON format
# Clue: Convert JSON -> List

from pprint import pprint

bank_accounts = json.loads(bank_data)

INTEREST_RATE = 0.1

for account in bank_accounts:
    if account["isActive"]:
        account["balance"] += account["balance"] * INTEREST_RATE

bank_accounts_json = json.dumps(bank_accounts, indent=4)
print(bank_accounts_json)  # ✅

# open() - write / read file
# with - auto close the file - no matter what

# open(<filename>, <mode>)

# Write a file
# with open("bank_accounts.json", "w") as file:
#     json.dump(bank_accounts, file, indent=4)


# Read a file
with open("bank_accounts.json", "r") as file:
    data = json.load(file)
    print(data, type(data))

# Task 1.1 (List comp)


# json.dumps  -> dumps as JSON
# json.dump  -> dumps as file (JSON)
# json.loads  -> loads into dict
# json.load  -> read as file (dict)


data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

import csv

with open("citizens.csv", "w", newline="") as file:
    writer = csv.writer(file)  # json.dump
    writer.writerows(data)


with open("citizens.csv", "r", newline="") as file:
    reader = csv.reader(file)  # json.dump
    data = [row for row in reader]
    print(data)

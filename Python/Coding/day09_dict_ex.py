employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]


for employee in employees:
    if "experience" in employee:
        employee["experience"] += 1
    else:
        employee["experience"] = 1
print(employees)


# Task: After 1 experience


# # Output
# [
#     {"name": "Sneha", "experience": 3},
#     {"name": "Manju",  "experience": 1},
#     {"name": "Sai Subash", "experience": 5},
#     {"name": "Manasa", "experience": 1},
# ]

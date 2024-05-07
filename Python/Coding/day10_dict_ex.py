employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]

# for employee in employees:
#     if "experience" in employee:
#         employee["experience"] += 1
#     else:
#         employee["experience"] = 1
# print(employees)

for employee in employees:
    employee["experience"] = employee.get("experience", 0) + 1
print(employees)

# Task: After 1 experience
# # Output
# [
#     {"name": "Sneha", "experience": 3},
#     {"name": "Manju",  "experience": 1},
#     {"name": "Sai Subash", "experience": 5},
#     {"name": "Manasa", "experience": 1},
# ]

# Task 2
#  Senior 5 or more, Mid-Level 3 to 5, Junior < 3
# Output
# [
#     {"name": "Sneha", "experience": 3, "status": "Mid-Level"},
#     {"name": "Manju", "experience": 1, "status": "Junior"},
#     {"name": "Sai Subash", "experience": 5, "status": "Senior"},
#     {"name": "Manasa", "experience": 1, "status": "Junior"},
# ]

# for employee in employees:
#     experience = employee["experience"]
#     if experience >= 5:
#         employee["status"] = "Senior"
#     elif experience >= 3:
#         employee["status"] = "Mid-Level"
#     else:
#         employee["status"] = "Junior"
# print(employees)

# for i in range(0,11):
#     print(i)


# While loop
# count = 1
# n = int(input())
# while count < n + 1:
#     print("✨" * count)
#     count += 1


# For loop
# n = int(input())
# for i in range(n + 1):
#     print("✨" * i)


# p = [10, 20, 30]
# for i in range(0, len(p)):
#     p[i] = p[i] * 2
# print(p)


avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]


# Output
# [4, 8, 11, 15, 10, 4]


# Task 4.1 - for loop
# lengths = []
# for avenger in avengers:
#     lengths.append(len(avenger))
# print(lengths)


# Task 4.2 - List comprehension - (Use this)
# lengths = [len(avenger) for avenger in avengers]
# print(lengths)

# Task 5.1
lengths = []
for avenger in avengers:
    if len(avenger) > 10:
        lengths.append(avenger)  # Append the avenger's name itself
print(lengths)

# Task 5.2
lengths = [avenger.upper() for avenger in avengers if len(avenger) > 10]
print(lengths)

# #print("Hello World!")

# # name = "Poojitha"
# # print(name)
# # print(type(name))

# # age = 20
# # print(age)

# # print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# name = input("What is your name? ")
# print("Hello my name is " + name + "!")

# Task 1 - Fahrenheit to Celsius

# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) * 5.0 / 9.0
# print("The equivalent of", fahrenheit, "F", celsius, "C")
# # F-strings
# {} - interpolation
# print(f"The equivalent of {fahrenheit} F is {celsius} C")

# Task 2 - Find age
# year = int(input("Enter the year you were born: "))
# age = 2024 - year
# expressions inside f-string
# print(f"You are {2024 - year} years old.")
# print(f"Your age is {age}")

# Task 3 - Find the area of a circle
# r = float(input("Enter the radius of the circle: "))
# area = 3.14 * r * r
# print(f"Area of the circle is {area}")

# Task 4 - Build a loader
n = int(input("Enter the loader number: "))
p = n // 10
loader = "[" + "=" * p + ">" + " " * (10 - p) + "]"
print(loader)

# Functions
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))


# Default Argument Values
def greet(name="Guest"):
    return f"Hello, {name}!"


print(greet())
print(greet("Alice"))


# Keyword Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")


display_info(age=25, name="John")


# Special Parameters
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)


# Arbitrary Argument Lists
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))

# Lambda Expressions
square = lambda x: x**2
print(square(5))

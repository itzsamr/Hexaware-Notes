from datetime import datetime

# Compile-time error (Syntax error)
# def math_divide(n1, n2):
#     try:
#         result = n1 / n2
#         return result

#     # Generic message
#     except:
#         return "Oops. 🤭 An Error happened"


# Errors
# 1. try
# 2. except
# 3. else
# 4. finally
def divide_eggs(n1, n2):
    try:
        # Business logic error
        if n1 < 0:
            # raise - throwing error
            raise ValueError("Eggs cannot be negative 🤭")
        if n2 < 0:
            raise ValueError("People cannot be negative 🤭")

        # Code is shield 🛡️
        result = n1 / n2

    # Specific message
    except ZeroDivisionError:
        return "You cannot divide by zero! 💀"
    except ValueError as e:
        return f"Invalid number: {e}"
    else:
        # When no error
        print("Division was successful ✅")
    finally:
        # No matter
        print("Operation done 😊✌️")

    return result


# Task 1: Handling string in birth_year


# Calculate age & Handle errors
# def calculate_age():
#     try:
#         current_year = datetime.now().year
#         birth_year = input("Please provide your birth year: ")

#         age = current_year - int(birth_year)
#         print(f"Your age is {age}")
#     except ValueError as err:
#         print("Invalid number: ", err)


# Task 2:  -ve value, future years (Logical Errors)


def calculate_age():
    try:
        current_year = datetime.now().year
        birth_year = int(input("Please provide your birth year: "))  # Runtime error

        if birth_year < 0:
            # Handling logical error
            raise ValueError("Year cannot be negative")
        if birth_year > current_year:
            raise ValueError("Your not flash to be from the future ⚡")

        age = current_year - birth_year
        print(f"Your age is {age}")
    except ValueError as err:
        print("Invalid number: ", err)
    except Exception as err:
        print("This catch all!", err)


def main():
    # Runtime error
    print(divide_eggs(10, -5))
    print(divide_eggs(-10, 5))
    print(divide_eggs(10, 5))
    print(divide_eggs(10, 0))  # Execution stops
    print(divide_eggs(15, 3))
    print(datetime.now().weekday())
    print(datetime.now().day)


# Every has same base class -> Exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed"
        super().__init__(self.message)

    # Overriding Base class __str__
    def __str__(self):
        return f"{self.value} -> {self.message}"


# Create you own Error Class


def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)
    except NegativeNumberError as err:
        print(err)


if __name__ == "__main__":
    # main()
    # calculate_age()
    only_positive_num()

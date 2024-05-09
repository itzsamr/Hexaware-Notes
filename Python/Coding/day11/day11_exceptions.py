# # Compile-time error (Syntax error)
# # def math_divide(n1, n2):
# #     try:
# #         result = n1 / n2
# #         return result

# #     # Generic message
# #     except:
# #         return "Oops. 🤭 An Error happened"


# # Errors
# # 1. try
# # 2. except
# # 3. else
# # 4. finally
# def divide_eggs(n1, n2):
#     try:
#         if n1 < 0:
#             raise ValueError("Eggs cannot be negative 🤭")
#         if n2 < 0:
#             raise ValueError("People cannot be negative 🤭")

#         # Code is shield 🛡️
#         result = n1 / n2

#     # Specific message
#     except ZeroDivisionError:
#         return "You cannot divide by zero! 💀"
#     except ValueError as e:
#         return f"Invalid number: {e}"
#     else:
#         # When no error
#         print("Division was successful ✅")
#     finally:
#         # No matter
#         print("Operation done 😊✌️")

#     return result


# # Runtime error
# print(divide_eggs(10, -5))
# print(divide_eggs(-10, 5))
# print(divide_eggs(10, 5))
# print(divide_eggs(10, 0))  # Execution stops
# print(divide_eggs(15, 3))

# # Handle error

# from datetime import datetime

# print(datetime.now().weekday())
# print(datetime.now().day)


# Calculate age & Handle errors
from datetime import datetime


def calculate_age():
    while True:
        try:
            birth_year = int(input("Please provide your birth year: "))
            if birth_year > datetime.now().year:
                print("You can't be born in the future!")
                continue
            elif birth_year < 0:
                print("Please enter a valid birth year.")
                continue
            else:
                current_year = datetime.now().year
                age = current_year - birth_year
                print(f"Your age is {age}")
                break
        except ValueError:
            print("Please enter a valid birth year as a number.")


calculate_age()

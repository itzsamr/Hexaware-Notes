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
        if n1 < 0:
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


# Runtime error
print(divide_eggs(10, -5))
print(divide_eggs(-10, 5))
print(divide_eggs(10, 5))
print(divide_eggs(10, 0))  # Execution stops
print(divide_eggs(15, 3))

# Handle error

from datetime import datetime

print(datetime.now().weekday())
print(datetime.now().day)


# Calculate age & Handle errors
def calculate_age():
    birth_year = input("Please provide your birth year: ")
    age = 2024 - int(birth_year)
    print(f"Your age is {age}")

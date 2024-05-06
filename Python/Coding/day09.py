# Statement vs Expression
# Expression -> Returns a value
# Statment -> Doesn't return anything

# nice = (9*8) > (100/2)

# g2 = 'Cool' if 5 > 7 else 'Super'
# print(g2)

# quote = "Dream"
# quote1 = "Dream is something"

# print(quote[-1]) # m
# print(quote[-4:-1]) # rea
# print(quote[::-1]) # maerD

# print(quote1[-1:-4:-1]) # gni


# fun = "madam"
# print(fun == fun[::-1])

# Task 2: Remove junk [*, (] to find the secret
message1 = "    🚨🔍📱🔑*******secret_code✌️((("
secret_message = message1.replace("*", "").replace("(", "")[message1.find('🔑')+1:]
print(secret_message.upper())
print(len(secret_message))


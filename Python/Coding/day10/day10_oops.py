# Idea
# Object Oriented Programming
# Modeling our problem as real-world objects

# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors


#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2


# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4


#  Car -> blueprint | Class blueprint object


# class Car:
#     def __init__(
#         self, name, engine, wheels, doors
#     ):  # creating object calls init (constructor)
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors

#     # Instance method
#     def horn(self):
#         return f"{self.name} says Vroom Vroom"


# ferrari = Car("Ferrari", "v8", 4, 2)  # object
# alto = Car("Alto", "v4", 4, 4)  # object
# sumo = Car("Suma", "v12", 4, 5)
# thar = Car("Thar", "v4", 4, 4)

# print(ferrari.name, ferrari.wheels)
# print(alto.name, alto.doors)
# print(sumo.engine, sumo.wheels)
# print(thar.name, thar.engine)
# print(type(ferrari))  # <class '__main__.Car'>
# print(ferrari.horn())

# Encapsulation: properties + action(logic)

# Task 1
class BankAcc:

    interest_rate = 0.02 # class variable

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    
    def display_balance(self):
        return f"The current balance is ₹.{self.balance:,}"
    
    def withdraw(self):
        amount = float(input("Enter the amount to be Withdrawed: "))
        if amount > self.balance:
            return "Insufficient Balance!"
        else:
            self.balance -= amount
            return f"Withdrawal Successful! Your new balance is ₹.{self.balance:,}"
    
    def deposit(self):
        amount = float(input("How much do you want to Deposit? "))
        self.balance += amount
        return f"The new balance is ₹.{self.display_balance()}"
    
    def interest(self):
        self.balance += self.balance * BankAcc.interest_rate
        return f"{self.display_balance()}"


amisha = BankAcc(101, "Amisha", 50_000)
mathesh = BankAcc(102, "Mathesh", 70_000)
sai = BankAcc(103, "Sai", 65_000)

# print(f"Account No : {amisha.acc_no}, Name : {amisha.name}, Balance : Rs.{amisha.balance}")
# print(f"\n Account No : {mathesh.acc_no}, Name : {mathesh.name}, Balance : Rs.{mathesh.balance}\n")
# print(f"\n Account No : {sai.acc_no}, Name : {sai.name}, Balance : Rs.{sai.balance}\n")

# Task 2
# print(amisha.display_balance())

# Task 3
# print(mathesh.withdraw())

#Task 4
# print(sai.deposit())

#Task 5 - interest rate
print(sai.interest())


# break -> stop loop
# continue -> skip one iteration
# return -> exits out of function


# def print_nums():
#     for num in range(1, 10):
#         if num == 6:
#             break

#         print(num)
#     print("Execution continues 🎊")


# def skip_even():
#     for num in range(1, 10):
#         if num % 2 == 0:
#             continue
#         print(num)
#     print("Execution continues 🎊")


# Task 1: Find the first negative value
# def first_negative(numbers):
#     for num in numbers:
#         if num < 0:
#             return num


# if __name__ == "__main__":
#     # print_nums()
#     # skip_even()
#     # Test case
#     print(first_negative([3, 5, 7, -1, 9, -3]))


# Task 2
# def process_until_duplicate(items):
#     x = set()
#     for i in items:
#         if i not in x:
#             print(f"processed {i}")
#             x.add(i)
#         else:
#             print(f"{i} Duplicate found")
#             return


# if __name__ == "__main__":
#     process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])


# Task 3
def censorship_bot(messages, banned_words):
    for message in messages:
        message_approved = True
        for banned_word in banned_words:
            if banned_word in message:
                message_approved = False
                break
        if message_approved:
            print(f"Approved message: {message}")
        else:
            print("Message isn't Approved")


messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!",
]

banned_words = ["bad", "oops"]

censorship_bot(messages, banned_words)

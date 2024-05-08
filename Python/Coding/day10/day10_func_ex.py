# library_list = [
#     {
#         "title": "Python Programming",
#         "author": "Eric Matthes",
#         "year": 2019,
#         "available": True,
#     },
#     {
#         "title": "Automate the Boring Stuff with Python",
#         "author": "Al Sweigart",
#         "year": 2020,
#         "available": True,
#     },
#     {
#         "title": "Learning Python I",
#         "author": "Mark Lutz",
#         "year": 2013,
#         "available": False,
#     },
#     {
#         "title": "Fluent Python",
#         "author": "Luciano Ramalho",
#         "year": 2015,
#         "available": True,
#     },
#     {
#         "title": "Adavance Python",
#         "author": "Mark Lutz",
#         "year": 2015,
#         "available": False,
#     },
# ]

# book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}

# Task 1
# Add Book Function: Write a function add_book(library, new_book)


# def add_book(library, new_book):
#     library.append(new_book)


# add_book(library_list, book)
# print(library_list)

# Task 2
# Search Books by Author Function: Write a function search_by_author(library, author_name)


# def search_by_author(library, author_name):
#     for book in library:
#         if book["author"] == author_name:
#             print(book)


# search_by_author(library_list, "Mark Lutz")


# def search_by_author(library, author_name):
#     return [book for book in library if book["author"] == author_name]


# print(search_by_author(library_list, "Mark Lutz"))

# Task 3
# Check Out Book Function: Write a function check_out_book(library, title) that marks a book as not available if it exists and is available in the library.


# def check_out_book(library, title):
#     for book in library:
#         if book["title"] == title and book["available"]:
#             book["available"] = False
#             print(f"Book '{title}' has been checked out.")
#             return
#     print(f"Book {title} not found or not available for check out.")


# title = "Fluent Python"
# check_out_book(library_list, title)

movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]


def get_average_rating(movie):
    rating_sum = sum(movie["ratings"])
    return round(rating_sum / len(movie["ratings"]))


sorted_movies = sorted(movies, key=get_average_rating, reverse=True)
print(sorted_movies)


# Arbitrary Arguments
def own_max(*nums):
    print(nums, type(nums))


own_max(5, 6, 10)
own_max(5, 6, 10, 7, 80, 60)


def own_max(*nums):
    # Implement max logic
    print(nums, type(nums))


own_max(5, 6, 10)
own_max(5, 6, 10, 7, 80, 60)


def own_max(*nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max


own_max(5, 6, 10)
own_max(5, 6, 10, 7, 80, 60)

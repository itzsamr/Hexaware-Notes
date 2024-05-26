# Class and Object
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"


my_dog = Dog("Buddy")
print(my_dog.bark())


# Access Specifiers
class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"


e = Example()
print(e.public)
print(e._protected)
# print(e.__private)  # This will raise an AttributeError


# Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 30)
print(person.name, person.age)


# Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


dog = Dog()
print(dog.speak())


# Polymorphism
class Cat:
    def sound(self):
        return "Meow"


class Dog:
    def sound(self):
        return "Bark"


def make_sound(animal):
    print(animal.sound())


cat = Cat()
dog = Dog()

make_sound(cat)
make_sound(dog)


# This is a single line comment

"""
This is a
multi-line
comment
"""

# Data Types and Variables
message = "Hello world!"  # This is a string
print(message)

number = 42  # This is an integer
print(number)

pi = 3.14159  # This is a float (decimal number)
print(pi)

# Data Structures
# List (Arrays)
fruits = ["apple", "banana", "orange"]
print(fruits)

# Adding to a list
fruits.append("grapes")
print(fruits)

# Removing from list
fruits.remove("banana")
print(fruits)

# Tuples
colors = ("red", "green", "blue")
print(colors)

# Dictionary (Objects)
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}
print(person)

# Loops
# For loop
for i in range(5):  # This will loop 5 times
    print(i)

# While loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Functions
def greet(name):
    return f"Hello, {name}!"


greeting = greet("Alice")
print(greeting)

# Conditional Statements
temperature = 30

if temperature > 28:
    print("It's hot!")
elif temperature < 10:
    print("It's cold!")
else:
    print("It's just right!")

# Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"


my_dog = Dog("Fluffy", "Golden Retriever")
print(my_dog.bark())


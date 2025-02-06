# Python Basics Learning Guide

"""
This file covers fundamental Python programming concepts:
1. Basic Data Types
2. Variables
3. Type Conversion
4. Lists, Tuples, and Dictionaries
5. Control Flow (Conditionals and Loops)
6. Functions
7. Exception Handling
8. List Comprehensions

Learning Objectives:
- Understand different data types in Python
- Learn how to declare and use variables
- Explore complex data structures
- Master control flow mechanisms
- Write and use functions
- Handle errors and exceptions
- Use advanced Python features like list comprehensions
"""

# 1. Basic Data Types and Variables
# Python is dynamically typed, meaning you don't need to declare variable types explicitly

# String: Represents text data
name = "Alice"  # String variable
print("String Example:")
print(f"Name: {name}, Type: {type(name)}")

# Integer: Whole numbers
age = 30  # Integer variable
print("\nInteger Example:")
print(f"Age: {age}, Type: {type(age)}")

# Float: Decimal numbers
height = 5.9  # Float variable
print("\nFloat Example:")
print(f"Height: {height}, Type: {type(height)}")

# Boolean: True or False values
is_student = True  # Boolean variable
print("\nBoolean Example:")
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# 2. Type Conversion
# Converting between different data types
number_string = "42"
converted_number = int(number_string)  # String to Integer
float_number = float(number_string)    # String to Float
print("\nType Conversion:")
print(f"Original String: {number_string}")
print(f"Converted to Integer: {converted_number}")
print(f"Converted to Float: {float_number}")

# 3. Complex Data Structures

# List: Ordered, mutable collection of items
fruits = ["apple", "banana", "cherry"]  # List declaration
print("\nList Examples:")
print("Original List:", fruits)
fruits.append("date")  # Adding an item
fruits[1] = "blueberry"  # Modifying an item
print("Modified List:", fruits)
print("List Slicing:", fruits[1:3])  # Getting a subset of the list

# Tuple: Ordered, immutable collection of items
coordinates = (10, 20)  # Tuple declaration
print("\nTuple Example:")
print("Coordinates:", coordinates)
# coordinates[0] = 15  # This would raise an error as tuples are immutable

# Dictionary: Key-value pairs
person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}  # Dictionary declaration
print("\nDictionary Example:")
print("Person Dictionary:", person)
print("Person's Name:", person["name"])
person["job"] = "Engineer"  # Adding a new key-value pair
print("Updated Dictionary:", person)

# 4. Control Flow

# If-Else Statements: Conditional execution
print("\nControl Flow - Conditionals:")
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For Loop: Iterate over a sequence
print("\nControl Flow - For Loop:")
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# Range-based For Loop
print("\nRange-based For Loop:")
for i in range(5):  # Generates numbers 0 to 4
    print(f"Current number: {i}")

# While Loop: Repeat while a condition is true
print("\nControl Flow - While Loop:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# 5. Functions: Reusable blocks of code
def greet(name, greeting="Hello"):
    """
    A function that generates a greeting.
    
    Args:
        name (str): The name to greet
        greeting (str, optional): The greeting message. Defaults to "Hello"
    
    Returns:
        str: A personalized greeting
    """
    return f"{greeting}, {name}!"

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Returns:
        float: Area of the rectangle
    """
    return length * width

print("\nFunction Examples:")
print(greet("Python Learner"))
print(greet("Alice", "Hi"))
print(f"Rectangle Area: {calculate_area(5, 3)} sq units")

# 6. Exception Handling: Managing errors
print("\nException Handling:")
try:
    # Potential error-causing code
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Exception handling block completed")

# 7. List Comprehensions: Concise way to create lists
print("\nList Comprehensions:")
# Create a list of squared numbers
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)

# Conditional list comprehension
even_squared_numbers = [x**2 for x in range(1, 6) if x % 2 == 0]
print("Even Squared Numbers:", even_squared_numbers)

# Bonus: Advanced Concepts Teaser
# Decorators, generators, lambda functions will be covered in advanced Python tutorials
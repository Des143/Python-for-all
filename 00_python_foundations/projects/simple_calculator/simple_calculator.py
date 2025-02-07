# Simple Calculator

# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform basic operations
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Handle division carefully
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
else:
    print("Cannot divide by zero!")

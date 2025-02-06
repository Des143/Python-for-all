# Basic Python Assignments

## Assignment 1: Personal Information Calculator
Write a program that:
1. Asks user for name, age, height, and weight
2. Calculates BMI
3. Prints formatted personal information

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kg: "))
    
    bmi = calculate_bmi(weight, height)
    
    print(f"\n--- Personal Information ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi:.2f}")

if __name__ == "__main__":
    main()

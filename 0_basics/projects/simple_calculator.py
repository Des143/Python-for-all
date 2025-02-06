# Basic Python Project: Simple Calculator

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    calc = Calculator()
    
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            break
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {calc.divide(num1, num2)}")
            else:
                print("Invalid choice!")
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

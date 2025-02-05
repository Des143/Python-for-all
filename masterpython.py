# Python Object-Oriented Programming (OOP) Tutorial

# 1. Basic Class Definition
class Person:
    """A basic class representing a person"""
    
    # Class Variable
    species = "Homo Sapiens"
    
    # Constructor Method
    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age
    
    # Instance Method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Class Method
    @classmethod
    def get_species(cls):
        return cls.species
    
    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18

# 2. Inheritance
class Student(Person):
    """A class representing a student, inheriting from Person"""
    
    def __init__(self, name, age, school):
        # Call parent class constructor
        super().__init__(name, age)
        self.school = school
    
    # Method Overriding
    def introduce(self):
        return f"{super().introduce()} I study at {self.school}."

# 3. Multiple Inheritance
class WorkingStudent(Student):
    """A class demonstrating multiple inheritance"""
    
    def __init__(self, name, age, school, job):
        super().__init__(name, age, school)
        self.job = job
    
    def describe_life(self):
        return f"I'm a student at {self.school} and I work as a {self.job}."

# 4. Encapsulation
class BankAccount:
    """A class demonstrating encapsulation"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

# 5. Polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Demonstration
def main():
    print("1. Basic Class and Object:")
    alice = Person("Alice", 25)
    print(alice.introduce())
    print("Species:", Person.get_species())
    print("Is Alice an adult?", Person.is_adult(alice.age))
    
    print("\n2. Inheritance:")
    bob = Student("Bob", 20, "Tech University")
    print(bob.introduce())
    
    print("\n3. Multiple Inheritance:")
    charlie = WorkingStudent("Charlie", 22, "Business School", "Intern")
    print(charlie.describe_life())
    
    print("\n4. Encapsulation:")
    account = BankAccount("David", 1000)
    print("Initial Balance:", account.get_balance())
    account.deposit(500)
    account.withdraw(200)
    print("Final Balance:", account.get_balance())
    
    print("\n5. Polymorphism:")
    shapes = [Rectangle(5, 3), Circle(4)]
    for shape in shapes:
        print(f"Shape Area: {shape.area()}")
#this is comment
print("hello")

if __name__ == "__main__":
    main()
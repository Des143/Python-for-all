# Python Variables: Storing and Managing Data

## 🎯 Learning Objectives
- Understand variable declaration
- Learn naming conventions
- Explore variable scope and mutability

## 📝 Variable Basics
```python
# Variable assignment
name = "Python Learner"
age = 25
height = 1.75

# Multiple assignment
x = y = z = 0

# Multiple variables
x, y, z = 1, 2, 3
```

## 🏷️ Naming Conventions
```python
# Good variable names
first_name = "John"
total_score = 100
is_active = True

# Avoid
1variable = "Invalid"  # Starts with number
class = "Reserved keyword"  # Reserved word
```

## 🔄 Variable Mutability
```python
# Mutable (can be changed)
numbers = [1, 2, 3]
numbers.append(4)  # Allowed

# Immutable (cannot be changed)
name = "Python"
# name[0] = 'p'  # This would raise an error
```

## 🧠 Memory and References
```python
# Reference example
a = [1, 2, 3]
b = a  # Both point to same list
b.append(4)  # Changes both a and b

# Using copy
import copy
a = [1, 2, 3]
b = copy.deepcopy(a)  # Independent copy
```

## 🚨 Variable Scope
```python
# Global variable
total = 0

def calculate():
    # Local variable
    local_total = 10
    global total
    total += local_total

calculate()
print(total)  # Accessing global variable
```

## 🛠 Best Practices
- Use descriptive names
- Follow snake_case convention
- Avoid single-character names
- Be consistent

## 🎲 Type Flexibility
```python
# Dynamic typing
x = 10        # Integer
x = "Hello"   # Now a string
x = [1, 2, 3] # Now a list
```

## 🚀 Practical Exercises
1. Create variables with different types
2. Experiment with variable assignment
3. Understand scope and mutability

## 📚 Key Concepts
- Variable declaration
- Naming rules
- Scope
- Memory management

## 📊 Self-Assessment
- Can you explain variable assignment?
- Do you understand mutable vs immutable?
- Can you create meaningful variable names?

**Keep Coding!** 🐍

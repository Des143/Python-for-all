# Python Type Conversion: Transforming Data Types

## 🎯 Learning Objectives
- Understand implicit and explicit type conversion
- Learn type casting techniques
- Handle conversion errors

## 🔄 Implicit Type Conversion
```python
# Automatic type conversion
x = 10    # Integer
y = 3.14  # Float
z = x + y # Automatically converts to float
```

## 🛠 Explicit Type Conversion
```python
# Integer conversions
num_str = "123"
num_int = int(num_str)  # String to Integer

# Float conversions
num_float = float("3.14")
num_int_from_float = int(3.14)  # Truncates decimal

# String conversions
str_num = str(42)
str_float = str(3.14)
```

## 🚨 Conversion Challenges
```python
# Potential errors
try:
    invalid = int("hello")  # Raises ValueError
except ValueError:
    print("Cannot convert non-numeric string")

# Safe conversion
def safe_convert(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
```

## 📊 Conversion Between Collections
```python
# List conversions
tuple_to_list = list((1, 2, 3))
set_to_list = list({1, 2, 3})

# Set conversions
list_to_set = set([1, 2, 2, 3])
tuple_to_set = set((1, 2, 3))

# Tuple conversions
list_to_tuple = tuple([1, 2, 3])
```

## 🧩 Advanced Conversions
```python
# Complex conversions
complex_num = complex(10)  # 10 + 0j
complex_from_str = complex("10+5j")

# Boolean conversions
bool_from_int = bool(1)   # True
bool_from_zero = bool(0)  # False
bool_from_str = bool("")  # False
```

## 🚀 Practical Scenarios
```python
# User input conversion
age = input("Enter your age: ")
age_int = int(age)  # Convert input to integer

# Data processing
prices = ["10.99", "20.50", "15.75"]
float_prices = [float(price) for price in prices]
```

## 🛡️ Best Practices
- Always handle potential conversion errors
- Use type hints for clarity
- Be explicit about conversions
- Validate input before conversion

## 📚 Key Concepts
- Implicit vs Explicit conversion
- Type casting
- Error handling
- Collection transformations

## 🎲 Conversion Limitations
- Not all types can be converted
- Precision loss in some conversions
- Context-dependent conversions

## 🚀 Practical Exercises
1. Convert between different types
2. Handle conversion errors
3. Create a type conversion utility function

## 📊 Self-Assessment
- Can you convert between basic types?
- Do you understand potential conversion issues?
- Can you safely convert user inputs?

**Keep Exploring Type Magic!** 🐍

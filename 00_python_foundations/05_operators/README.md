# Python Operators: Mastering Data Manipulation

## 🎯 Learning Objectives
- Understand different types of operators
- Learn operator precedence
- Explore practical operator usage

## 🧮 Arithmetic Operators
```python
# Basic arithmetic
x = 10
y = 3

addition = x + y       # 13
subtraction = x - y    # 7
multiplication = x * y # 30
division = x / y       # 3.333
floor_division = x // y # 3
modulus = x % y        # 1
exponentiation = x ** y # 1000
```

## 🔍 Comparison Operators
```python
# Comparing values
a = 5
b = 10

equal = a == b         # False
not_equal = a != b     # True
greater = a > b        # False
less = a < b           # True
greater_equal = a >= b # False
less_equal = a <= b    # True
```

## 🧩 Logical Operators
```python
# Combining conditions
is_sunny = True
is_warm = False

and_operator = is_sunny and is_warm  # False
or_operator = is_sunny or is_warm    # True
not_operator = not is_sunny          # False
```

## 🔢 Bitwise Operators
```python
# Bit-level operations
x = 5    # 101 in binary
y = 3    # 011 in binary

bitwise_and = x & y     # 1
bitwise_or = x | y      # 7
bitwise_xor = x ^ y     # 6
left_shift = x << 1     # 10
right_shift = x >> 1    # 2
```

## 🧠 Assignment Operators
```python
# Combining assignment with operation
a = 10
a += 5   # Equivalent to a = a + 5
a -= 3   # Equivalent to a = a - 3
a *= 2   # Equivalent to a = a * 2
a /= 2   # Equivalent to a = a / 2
```

## 🚀 Identity and Membership Operators
```python
# Checking identity and membership
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Identity operators
print(list1 is list3)    # True
print(list1 is list2)    # False

# Membership operators
print(2 in list1)        # True
print(4 not in list1)    # True
```

## 🎲 Operator Precedence
```python
# Understanding operator order
result = 2 + 3 * 4      # 14, not 20
complex_expr = (2 + 3) * 4  # 20
```

## 🛠 Practical Exercises
1. Create expressions using different operators
2. Experiment with operator precedence
3. Build a simple calculator

## 📚 Key Concepts
- Operator types
- Precedence rules
- Type-specific behaviors
- Performance considerations

## 🚨 Common Pitfalls
- Floating-point precision
- Integer division behavior
- Mutable vs immutable comparisons

## 🌟 Advanced Techniques
- Chaining comparisons
- Using operators with custom classes
- Operator overloading

## 📊 Self-Assessment
- Can you explain different operator types?
- Do you understand operator precedence?
- Can you predict operator results?

**Operator Mastery Awaits!** 🐍

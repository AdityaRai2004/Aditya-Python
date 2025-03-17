# Variables in Python

## Definition
A **variable** in Python is a named storage location that holds a value. Variables allow programmers to store, retrieve, and manipulate data during program execution.

## Variable Declaration and Assignment
```python
x = 10  # Assigning an integer to a variable
y = 3.14  # Assigning a float to a variable
name = "Alice"  # Assigning a string to a variable
```

## Rules for Naming Variables
1. Must start with a letter (a-z, A-Z) or an underscore (_).
2. Can contain letters, digits (0-9), and underscores.
3. Cannot use Python keywords (e.g., `if`, `while`, `class`).
4. Case-sensitive (`var` and `Var` are different variables).

## Example Usage
```python
age = 25
height = 5.9
greeting = "Hello, World!"
print(age, height, greeting)
```

## Variable Types
- **Integer (`int`)**: Whole numbers (e.g., `5`, `100`)
- **Floating-Point (`float`)**: Decimal numbers (e.g., `3.14`, `2.71`)
- **String (`str`)**: Text values (e.g., "Python", "Hello")
- **Boolean (`bool`)**: `True` or `False`

## Research: How Python Stores Variables in Memory
- In Python, variables are references to objects stored in memory.
- When a variable is assigned a value, Python creates an object in memory and binds the variable name to it.
- If a new value is assigned to a variable, Python creates a new object and reassigns the variable to reference the new object.
- Python uses **Garbage Collection** to free memory from unused objects.

## Exercise: Assign Values and Observe Changes
```python
x = 10  # Initial assignment
print("Initial x:", x)

x = 20  # Reassignment
print("Updated x:", x)

x = "Python"  # Changing type
print("Changed x:", x)
```



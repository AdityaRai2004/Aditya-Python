# Assigning a Function to a Variable

## Definition
In Python, functions are first-class objects, meaning they can be assigned to variables and called using the new variable name.

## Example
```python
def square(num):
    return num * num

sq = square  # Assigning the function to a variable
result = sq(4)  # Calling the function using the new variable
print(result)  # Output: 16
```

## Explanation
1. **Function Definition**: The `square` function is defined to take a number and return its square.
2. **Assignment**: The function `square` is assigned to the variable `sq`.
3. **Function Call via Variable**: The function is invoked using `sq(4)`, which is equivalent to `square(4)`.
4. **Output**: The result `16` is printed.



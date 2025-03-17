# Reserved Keywords in Python

## Definition
Reserved keywords in Python are predefined words that cannot be used as variable names, function names, or identifiers.

## Exercise: Using Reserved Keywords as Variables
```python
class = "Math"  # This will cause a SyntaxError
if = 10  # This will also cause a SyntaxError
```

## Fun Fact: Listing Python Keywords
Python provides a way to list all reserved keywords using the `keyword` module.
```python
import keyword
print(keyword.kwlist)  # Prints all Python reserved keywords
```

## Why Reserved Keywords Matter
- They have special meanings in Python.
- Using them incorrectly results in errors.
- Helps maintain readability and consistency in coding.

## Common Reserved Keywords in Python
Some examples of Python's reserved keywords include:
- `if`, `else`, `while`, `for`
- `class`, `def`, `return`, `import`
- `try`, `except`, `finally`, `raise`
- `True`, `False`, `None`

Avoid using these words as variable names to prevent errors in your code.


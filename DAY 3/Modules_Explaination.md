### 1. Investigate Circular Imports

Fix the circular import problem between `module_a.py` and `module_b.py`.

#### module_a.py:

```python
import module_b

def func_a():
    return "Function A"

print(module_b.func_b())
```

#### module_b.py:

```python
import module_a

def func_b():
    return "Function B"
```
 Explaination:

We can use local imports

### 2. Dynamic Module Loading

Write a program that dynamically imports and executes a function from any module specified by the user.
Example:

```shell

Enter module name: math
Enter function name: sqrt
Enter argument: 25
Output: 5.0

```
Explaination:

```python

import math

def sqrt(number):
    return math.sqrt(number)

number = int(input("Enter argument : "))
print("Square root of the number is : ", sqrt(number))

```
### 3. Custom Module with Exception Handling

Create a custom module `calculator.py` that handles division by zero and invalid inputs gracefully.

```python
# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
```
Explaination:

First Imported and Executed it using this code

```python

import calculator

result = calculator.divide(10,5)
print(result)

result = calculator.divide(8,0)
print(result)

result = calculator.divide(5,10)
print(result)

result = calculator.divide(10,'abc')
print(result)

```
### 4. Advanced Import Strategies

Write a script that:

- Imports a module.
- Checks if a function exists.
- Executes it if available, otherwise gracefully handles the error.

Solution:

#### custom_module.py 

```python

def my_function():
    print("Hello World")

```
#### Checking its Availability

```python

import custom_module

if hasattr(custom_module, "my_function"):
    my_func = getattr(custom_module, "my_function")
    if callable(my_func):
        print(my_func)
    else:
        print("The Function cannot be found")

```

### 5. Optimize Import Time

Use `time` module to measure import time for different methods (single import vs. importing everything).

```python

import time
start_time = time.time()
import math
end_time = time.perf_counter() 
print(f"Time taken for single import (math): {end_time - start_time:.4f} seconds")

start_time = time.time()
from math import *
end_time = time.perf_counter()
print(f"Time taken for 'from math import *': {end_time - start_time:.4f} seconds")

```
Explaination:

1. time.perf_counter():

 - Provides high-resolution timing, ideal for measuring short durations like import times.

- Captures the current time before and after the import

### 6. Module Creation and Distribution

Implemented using this diagram

    sound/
    __init__.py
    effects/
        __init__.py
        echo.py
        surround.py
    filters/
        __init__.py
        equalizer.py

### 8. Mocking Modules for Testing

Write a unit test for a function that imports a module. Use `unittest.mock` to mock the imported module.

```python
from unittest import mock
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # Should print 100
```

Solution:

# mymodule.py

```python

import math

def calculate_square_root(number):
    return math.sqrt(number)

```

# test_mymodule.py

```python

import unittest
from unittest.mock import patch
from my_module import calculate_square_root

class TestSquareRoot(unittest.TestCase):
    @patch('mymodule.math.sqrt')  # Mock the math.sqrt imported in mymodule
    def test_calculate_square_root(self, mock_sqrt):
        # Configure mock to return a fixed value
        mock_sqrt.return_value = 100
        
        # Test the function
        result = calculate_square_root(25)
        
        # Verify the result and mock usage
        self.assertEqual(result, 100)
        mock_sqrt.assert_called_once_with(25)

if __name__ == '__main__':
    unittest.main()

```

### 9. Import Side Effects

Investigate modules that run code at import time. Create a module that prints something as soon as it’s imported.

```python

# Square.py
print("This code runs as soon as the module is imported in the program")

def greet(name):

    return f"Hello" {name}   

#test_square.py

from Square import greet

```

Explaination:

So we Create a file in which we print something as soon as the module is imported. This is done by simply printing a message in the file and creating a function by which we can call the function and see the output. This is a simple example of side effect in python.




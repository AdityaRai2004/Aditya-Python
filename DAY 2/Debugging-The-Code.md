## Advanced Debugging Techniques

### 1. Error Classification

```python

for i in range(5)
    print(i)

x = 10 / 0

def calculate_area(radius):
    return 2 * 3.14 * radius 

```
#### Errors
Syntax Error: There is a missing colon in the first line of the for loop.

ZeroDivisionError: The number cannot be divided by zero, as it will raise a ZeroDivisionError.

Incorrect Formula: The formula for the area of a circle is not correct. The correct formula should be:

Area = π * radius²

### 2. Debugging Complex Functions

```python

def process_data(data):
    total = 0
    for item in data:
        total += int(item)
    return total / len(data)

print(process_data(['10', '20', 'abc', '30']))

```
#### Errors
ValueError: The function will raise a ValueError when it encounters a non-numeric value in the data

### 3. Advanced Debugging Challenge

```python

def unreliable_function():
    number = random.choice([0, 1, 2])
    return 10 / number

for i in range(10):
    print(unreliable_function())

```
#### Errors
ZeroDivisionError: The function will raise a ZeroDivisionError when it encounters a zero in the random

### 4. Writing Debug-Friendly Code
```python

def calculate_discount(price, discount):
    return price - (price * discount / 100)

print(calculate_discount(100, '10%'))

```
#### Errors
TypeError: The function will raise a TypeError when it encounters a non-numeric value for the discount

Value Error: The function will raise a ValueError when it encounters a non-numeric value for the discount





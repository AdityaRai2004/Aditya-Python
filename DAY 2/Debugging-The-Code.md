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
print(calculate_discount(100, 'abc')) 

```
#### Errors
TypeError: The function will raise a TypeError when it encounters a non-numeric value for the discount

Value Error: The function will raise a ValueError when it encounters a non-numeric value for the discount

### 5. Rubber Duck Debugging

```python

numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("Product:", result)

```
#### Explaination

Initialization of List:

numbers = [1, 2, 3, 4,ed numbers` is created containing the integers 1 through 5.

Initialization of Result:

result = 1: A variable named result is initialized to 1, serving as the starting point for multiplication.

For Loop:

for num in numbers:: This loop iterates over each number in the numbers list

Multiplication:

Inside the loop:

result *= num: The current value of result is multiplied by num, and the result is stored back in result.

Final Output:

print("Product:", result): After the loop completes, this line prints the final product of all numbers in the list.

Final Result
The final output displayed will be: 120

### 6. Advanced Challenge: Debug a Multi-threaded Program

```python

import threading

counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Expected: 200000

```
### 8. Memory Leaks and Performance Debugging

```python
import time
def efficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2) # the function sleeps for 2 seconds hence inefficent
        time.sleep(2)
    return result

print(len(efficient_function()))
```
#### Errors

-This function sleeps for 2 milliseconds which for a large for loop creates a lot of time inefficiency

### 9. Debug why the function returns None:

```python

def add(a, b):
    return result = a + b #missing return
print(add(3, 4))

```
#### Errors

there was a missing retun statement in the function hence when printed it showed a none type as output

### 10. Silent Failures

```python
try:
    result = 10 / 0
except:
    pass
print("No error detected!")

```
#### Errors

    This except block does not handle the divide by zero error and the try block does not allow the expression to raise an error becuase it expects the except block to handle it








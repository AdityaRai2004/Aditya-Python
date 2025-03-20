## 1. Introduction to Sequences

In Python, a **sequence** is an ordered collection of items. The order of elements is preserved, and each element is accessible via its index.

The main types of sequences in Python are:

- Strings
- Lists
- Tuples

## 2. Differentiation between the Three Sequences

Strings: Strings are sequences of characters enclosed in quotes. They are immutable, meaning their contents cannot be modified after initialisation.

Lists:

Definition: A list is a mutable sequence of items that can store elements of any data type.

Mutability: Mutable — you can add, remove, or modify its elements.  

Usage: Ideal for dynamic collections of homogeneous or heterogeneous data.

Syntax:

```python

my_list = [1, 2, 3, "apple", [4, 5]]

```
Key Features:

Supports indexing, slicing, nesting (e.g., lists within lists).

Methods include .append(), .remove(), .pop(), .sort(), etc.

Tuples

Definition: A tuple is an immutable sequence of items that can store elements of any data type.

Mutability: Immutable — once created, the contents cannot be changed.

Usage: Best for fixed collections of heterogeneous data where immutability is desired.

Syntax:

```python

my_tuple = (1, "apple", [3, 4])

```

Single-element tuples require a trailing comma: (42,).

Key Features:

Supports indexing and slicing but not modification.

Tuples are hashable (can be used as dictionary keys) if they contain only immutable elements.

## 3. How Indexing Works

Indexing is based on (0-19...) it generally gives the character a unique identity that allows the user to find the character in the string. The index of the first character is 0, the index of the second is 1 etc. It is generally the same in Lists and Tuples

General Indexing Rules

Zero-based indexing: The first element has an index of 0, the second 1, and so on.

Negative indexing: Allows access from the end of the sequence, where -1 represents the last element, -2 the second last, etc.

Syntax: Uses square brackets [] to specify the index:

```python

my_list = [10, 20, 30]
print(my_list[0])  # Output: 10
print(my_list[-1]) # Output: 30

```
## 4. Last Character Access

```python
#Creating a String
str = "Hello World"

#Accessing the Last Character
last_ch = str[-1]

#Printing the Character
print(last_ch)

```

## 5. Access Third Element

```python


numbers = [1, 2, 3, 4]
num = numbers[2]
print(num)

```

## 6. Result Of Length of Elements

```python

numbers = ([1 , [2, 3] , 4])
length = len(numbers)
print(length)

```

Output: The Answer is Three

Explaination : This is because the len() function counts the number of elements in a list, and in this case, u can see there is list inside a list and it is considered a single element. So the total number of elements is 3.

## 7. Slicing

Slixixng is a way to extract a subset of elements from a list. It is done by specifying the start and the end of a list, string and tuple.

```python 

numbers = [0, 1, 2, 3, 5, 6]
print(numbers[1:4]) # Output: [1, 2, 3]

```

## 8. Reversing a String using Slicing

```python

# Define a string
my_string = "Hello, World!"

# Reverse the string using slicing
reversed_string = my_string[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

```
Explaination: 

Slicing Syntax: The general slicing syntax is [start:stop:step].

start: The starting index (default is 0).

stop: The ending index (default is the length of the string).

step: The step size or increment (negative values traverse backward).

## 9. List Concantenation and Repitition

```python

list1 = [1, 2, 3, 4]
list2 = [2, 4, 5, 6, 8]
result = list1 + list2
print(result)

```
Explaination: This is a way to combine two lists into one. The + operator is used.

```python

list1 = [2,4,5,6] * 7
print(list1)

```
## 10. Counting Occurences

```python

list1 = [1,2,3,4,5,6,7,2,5,36,52,34,6,5,4]
print(list1.count(2), list1.count(4), list1.count(5))

```
## 11. Output of a Tuple that is sliced

```python

my_tuple = (1,2,3)
print(my_tuple[1:]) # Output : 2,3

```

## 12.  Difference between list.append() and list.extend()

Solution: 

The difference between list.append() and list.extend() in Python lies in how they add elements to a list:

list.append():

Functionality: Adds a single element (object) to the end of the list.

Behavior: The entire object, regardless of its type, is added as a single item.

Use Case: Use when you want to add one item (e.g., a number, string, or another list) to the list.

Example:

```python

my_list = [1, 2, 3]
my_list.append([4, 5])  # Appends the list [4, 5] as a single element
print(my_list)          # Output: [1, 2, 3, [4, 5]]

```

list.extend()

Functionality: Adds all elements of an iterable (e.g., list, tuple, string) to the end of the list.

Behavior: Each element from the iterable is added individually to the list.

Use Case: Use when you want to merge multiple elements from an iterable into the list.

Example:

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])  # Extends the list by adding each element from [4, 5]
print(my_list)          # Output: [1, 2, 3, 4, 5]

```

## 13. Spliting Sentence into individual characters

```python

sen = "Learn Python, step by step!" 
val = sen.split()

```

## 14. Joining a list into a Single String

```python

# Define the list
my_list = ['Python', 'is', 'fun']

# Join the list into a single string with spaces as separators
result = ' '.join(my_list)

# Print the result
print(result)

```

## 15. Finding occurences

```python

numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))

```

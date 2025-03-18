#1
for i in range(5):
    print(i)
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot be Divided by Zero")
    
def calculate_area(radius):
    return 3.14 * radius * radius

#2

def process_data(data):
    total = 0
    count = 0  # To keep track of valid numeric entries or the number of items that have been passed
    for item in data:
        try:
            total += int(item)
            count += 1
        except ValueError:
            print(f"Warning: '{item}' is not a valid number and will be skipped.")
    
    if count == 0:  # Avoid division by zero generally can lead to total failure
        return 0
    
    return total / count

print(process_data(['10', '20', 'abc', '30']))

#3

import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    try:
        return 10 / number
    except ZeroDivisionError:
        print("Cannot be divided by zero")

for i in range(10):
    print(unreliable_function())
    
#4
    
def calculate_discount(price, discount):
    try:
        if isinstance (discount, str) and discount.endswith('%'):
            discount = float(discount[:-1])
        else:
            discount = float(discount)
        
        return price - (price * discount / 100)
    except TypeError and ValueError:
        print("Warning: Wrong data type for discount")
        return None

print(calculate_discount(100, '10%'))
print(calculate_discount(100, 'abc')) 




    
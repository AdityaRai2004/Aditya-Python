"""
total = 0
target = 10
for i in range(11):
    total = target * i
    print(total)
    
"""

def multiplication_table(n):
    # Print the multiplication table up to n x n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Print the product with a formatted string
            print(f"{i * j:4}", end=' ')
        print()  # New line after each row

table_size = 10
multiplication_table(table_size)

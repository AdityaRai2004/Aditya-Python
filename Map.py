list_of_integer = ["123", "456", "abc", "789", "def", "012"]
filtered_integers = list(filter(lambda x: x[0] in "1234567890", list_of_integer))
print(filtered_integers)


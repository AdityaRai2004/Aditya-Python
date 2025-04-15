import os

# Use a raw string (prefix with r) to avoid issues with backslashes
path = r'C:\Users\Aditya\Desktop\Python\DAY 10'

try:
    entries = os.listdir(path)
    print(f"Contents of '{path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory {path} does not exist.")
except NotADirectoryError:
    print(f"The path {path} is not a directory.")
except PermissionError:
    print(f"Permission denied to access {path}.")

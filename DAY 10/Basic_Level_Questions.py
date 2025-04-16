# Open the file 'notes.txt' in read mode
with open('notes.txt', 'r') as file:
    # Read and print each line
    for line in file:
        print(line, end='')  # end='' prevents adding extra newlines
        
#2
line_count = 0
with open('poem.txt', 'r') as file:
    for line in file:
        line_count += 1

print(f"Total lines in poem.txt: {line_count}")

#3
tasks = [
    "Buy groceries",
    "Call mom",
    "Finish homework",
    "Clean the room",
    "Read a book"
]

with open('reminder.txt', 'w') as file:
    for task in tasks:
        file.write(task + '\n')
        
#4
new_task = "Go for a walk"

with open('reminder.txt', 'a') as file:
    file.write(new_task + '\n')
    
#5
import os

filename = 'data.txt'

if os.path.exists(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
else:
    print(f"{filename} does not exist.")


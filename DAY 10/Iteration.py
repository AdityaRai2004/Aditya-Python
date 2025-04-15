'''with open('example.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())
'''
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
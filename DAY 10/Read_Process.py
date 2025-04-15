filename = "example.txt"
with open(filename, "r") as file:
    for line in file:
        process_line = line.strip().upper()
        print(process_line)
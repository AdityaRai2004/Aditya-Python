# List of input files to merge
input_files = ['chapter1.txt', 'chapter2.txt', 'chapter3.txt']

# Output file
output_file = 'full_book.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for fname in input_files:
        with open(fname, 'r', encoding='utf-8') as infile:
            contents = infile.read()
            outfile.write(contents)
            outfile.write('\n')  # Optional: add a newline between chapters

print(f"Files merged successfully into {output_file}")


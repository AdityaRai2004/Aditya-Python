#6
with open('input.txt') as infile, open('cleaned.txt', 'w') as outfile:
    outfile.writelines(line for line in infile if line.strip())
    
#7
with open('article.txt') as infile, open('article_modified.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.replace('Python', 'PYTHON'))

#8
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.upper())
        
#9
with open('students.txt') as infile, open('report.txt', 'w') as outfile:
    for line in infile:
        name, marks = line.strip().split(',')
        status = 'Pass' if int(marks) >= 50 else 'Fail'
        outfile.write(f"{name},{status}\n")
    
#10
with open('quotes.txt') as infile, open('reversed_quotes.txt', 'w') as outfile:
    lines = infile.readlines()
    outfile.writelines(reversed(lines))



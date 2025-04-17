with open('raw_text.txt', 'r', encoding='utf-8') as infile, \
     open('raw_text_formatted.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        clean_line = line.strip().replace('\t', ' ')
        outfile.write(clean_line + '\n')

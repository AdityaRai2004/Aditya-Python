import csv

with open('products.csv', 'r', encoding='utf-8')as infile:
    reader = csv.DictReader(infile)
    data = list(reader)
    
    sorted_data = sorted(data, key = lambda x : float(x['price']))
    
    with open('products_sorted.csv', 'w', newline =' ',encoding='utf-8')as outfile:
        writer = csv.writer(outfile)
        writer.writeheader()
        writer.writerow(sorted_data)
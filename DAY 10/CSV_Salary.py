import csv

def filter_sales(input_files = 'sales.csv' , output_file = 'high_sales.csv', threshold = 10000):
    with open ('sales.csv' , 'r', newline='') as file, open ('high_sales.csv', 'w', newline='') as file2:
        
        reader = csv.Dictreader(file)
        writer = csv.Dictwriter(file2)
        
        writer.writeheader()
        
    for row in reader:
            try:
                 amount = float(row.get('amount', 0)) 
                 if amount > threshold:
                    writer.writerow(row)
                    print(f"{row}")
            except (ValueError, TypeError):
                         print(f"Skipping malformed entry: {row}")
    filter_sales()

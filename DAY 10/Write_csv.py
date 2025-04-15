import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Charlie', '22', 'Chicago'])
    writer.writerow(['Aditya', '24', 'Mumbai'])
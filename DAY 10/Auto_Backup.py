import csv
import os
from datetime import datetime

# Define source and backup directory
source_file = 'data.csv'
backup_dir = 'backup'

# Ensure the backup directory exists
os.makedirs(backup_dir, exist_ok=True)

# Format current date as YYYYMMDD
current_date = datetime.now().strftime('%Y%m%d')

# Construct backup filename with date
backup_file = os.path.join(backup_dir, f'data_backup_{current_date}.csv')

# Copy contents from source to backup file
with open(source_file, 'r', newline='', encoding='utf-8') as src, \
     open(backup_file, 'w', newline='', encoding='utf-8') as dst:
    reader = csv.reader(src)
    writer = csv.writer(dst)
    for row in reader:
        writer.writerow(row)

print(f'Backup created: {backup_file}')

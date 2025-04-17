import csv
import os
from datetime import datetime

source_file = 'data.csv'
backup_dir = 'backup'

os.makedirs(backup_dir, exist_ok=True)


current_date = datetime.now().strftime('%Y%m%d')

backup_file = os.path.join(backup_dir, f'data_backup_{current_date}.csv')


with open(source_file, 'r', newline='', encoding='utf-8') as src, \
     open(backup_file, 'w', newline='', encoding='utf-8') as dst:
    reader = csv.reader(src)
    writer = csv.writer(dst)
    for row in reader:
        writer.writerow(row)

print(f'Backup created: {backup_file}')

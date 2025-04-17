import shutil
import os
from datetime import date

backup_folder = 'backup'
os.makedirs(backup_folder, exist_ok=True)

today = date.today().strftime("%Y%M%D")

new_filename = f"data_backup_{today}.csv"

shutil.copy("data.csv", os.path.join(backup_folder, new_filename))

print(f"Backup created: {backup_folder}/{new_filename}")
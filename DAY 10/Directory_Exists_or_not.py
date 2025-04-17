import os

def list_txt_csv_files(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and (filename.lower().endswith('.txt') or filename.lower().endswith('.csv')):
            files.append(filename)
    return files

directory_path = '/path/to/your/folder'
result = list_txt_csv_files(directory_path)
print("TXT or CSV files found:")
for file in result:
    print(file)

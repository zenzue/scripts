import json
import csv
import sys

json_file = sys.argv[1]

with open(json_file) as file:
    data = json.load(file)

keys = list(data.keys())

banner = '''
╔═══════════════════════╗
║   Written by w01f     ║
╚═══════════════════════╝
'''

print(banner)

csv_file = json_file.replace('.json', '.csv')
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Key', 'Value'])

    
    for key in keys:
        value = data[key]
        writer.writerow([key, value])

print(f'Conversion successful. CSV file saved as {csv_file}')
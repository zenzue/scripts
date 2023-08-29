import csv
import json
import sys

csv_file = sys.argv[1]

banner = '''
╔═════════════════════════════════════╗
║    CSV to JSON Conversion  by w01f  ║
╚═════════════════════════════════════╝
'''

print(banner)

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

json_data = json.dumps(data, indent=4)

json_file = csv_file.replace('.csv', '.json')
with open(json_file, 'w') as file:
    file.write(json_data)

print(f'Conversion successful. JSON file saved as {json_file}')

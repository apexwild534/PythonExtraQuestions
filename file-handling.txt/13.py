import csv

with open('inventory.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

for item in data:
    current_quantity = int(item['Quantity'])
    new_quantity = int(current_quantity * 1.10)
    item['Quantity'] = str(new_quantity)

with open('inventory.csv', 'w', newline='') as file:  #THE CHANGE IS DONE IN THE SAME FILE WITHOUT CREATING A NEW FILE
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(data)

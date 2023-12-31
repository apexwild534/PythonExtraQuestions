import csv

with open('sales.csv', 'r') as input_file, open('high_revenue_sales.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        revenue = float(row['Revenue'])
        if revenue > 1000:
            writer.writerow(row)

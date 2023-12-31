import csv

total_price = 0
product_count = 0

with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row['Price'])
        total_price += price
        product_count += 1

if product_count > 0:
    average_price = total_price / product_count
    print(f"Average Price of Products: ${average_price:.2f}")
else:
    print("No products found in the file.")

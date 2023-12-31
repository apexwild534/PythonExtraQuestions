def calculate_total_sales(transactions):
    category_sales = {}

    for transaction in transactions:
        product_name = transaction['product']
        category = transaction['category']
        amount = transaction['amount']

        if category in category_sales:
            category_sales[category] += amount
        else:
            category_sales[category] = amount

    return category_sales

# Example list of sales transactions (list of dictionaries)
sales_transactions = [
    {'product': 'Product A', 'category': 'Electronics', 'amount': 1000},
    {'product': 'Product B', 'category': 'Electronics', 'amount': 800},
    {'product': 'Product C', 'category': 'Clothing', 'amount': 250},
    {'product': 'Product D', 'category': 'Electronics', 'amount': 1200},
    {'product': 'Product E', 'category': 'Clothing', 'amount': 300},
    {'product': 'Product F', 'category': 'Furniture', 'amount': 500},
]

category_sales = calculate_total_sales(sales_transactions)

# Display total sales for each category
for category, total_sales in category_sales.items():
    print(f"Category: {category}, Total Sales: ${total_sales}")

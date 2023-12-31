def calculate_total_cost(shopping_cart, item_prices):
    total_cost = 0

    for item in shopping_cart:
        if item in item_prices:
            total_cost += item_prices[item]
        else:
            print(f"The item '{item}' does not exist in the item prices dictionary.")

    return total_cost

# Example usage:

item_prices = {
    'apple': 0.50,
    'banana': 0.25,
    'orange': 0.30,
    'pear': 0.40
}

shopping_cart = ['apple', 'banana', 'orange', 'pear']

total_cost = calculate_total_cost(shopping_cart, item_prices)

print(f"The total cost of items in the shopping cart is ${total_cost}.")
def group_items_by_criterion(items):
    groups = {'odd': [], 'even': []}
    
    for item in items:
        if item % 2 == 0:
            groups['even'].append(item)
        else:
            groups['odd'].append(item)
    
    return groups

# Example usage:
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = group_items_by_criterion(items)

print("Odd numbers:", result['odd'])
print("Even numbers:", result['even'])

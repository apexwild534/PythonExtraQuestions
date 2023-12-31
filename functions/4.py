def find_max_value(numbers):
    if not numbers:
        return None  # Handle the case of an empty list
    return max(numbers)

numbers = [10, 25, 7, 42, 15]
max_value = find_max_value(numbers)
print(max_value)  # This will print 42

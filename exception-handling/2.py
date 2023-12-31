def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result

# Test the function
print(divide(10, 2)) # Output: 5.0
print(divide(10, 0)) # Output: Error: Division by zero is not allowed.
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of the division is: {result}")

# Test the function
divide(10, 2)
divide(10, 0)
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        factorial = 1
        while n > 0:
            factorial *= n
            n -= 1
        return factorial

# Example usage:
number = 5
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")

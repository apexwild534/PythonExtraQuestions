def factorial_with_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# Example usage:
number = 5
factorial = factorial_with_loop(number)
print(f"The factorial of {number} is {factorial}")

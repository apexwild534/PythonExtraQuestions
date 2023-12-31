def find_nth_fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        count = 2  # We've already calculated the first two Fibonacci numbers

        while count < n:
            a, b = b, a + b
            count += 1

        return b

# Example usage:
n = 10
result = find_nth_fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

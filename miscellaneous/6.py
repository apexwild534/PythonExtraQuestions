def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

# Example usage:
n = 10  # Change n to the desired term
fibonacci_sequence = generate_fibonacci_sequence(n)
print(f"Fibonacci sequence up to the {n}th term:", fibonacci_sequence)

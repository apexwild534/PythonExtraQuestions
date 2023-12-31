def print_diamond(n):
    # Print the top half of the diamond
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)

    # Print the bottom half of the diamond
    for i in range(n - 2, 0, -2):
        print(' ' * ((n - i) // 2) + '*' * i)

# Example usage:
size = 5
print_diamond(size)

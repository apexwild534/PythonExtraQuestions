def print_number_triangle(n):
    for i in range(1, n + 1):
        # Print spaces before the numbers
        print(' ' * (n - i), end='')

        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end=' ')

        # Move to the next line
        print()

# Example usage:
height = 5
print_number_triangle(height)

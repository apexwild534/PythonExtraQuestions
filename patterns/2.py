def print_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            # Print the top and bottom rows as full asterisks
            print('*' * n)
        else:
            # For other rows, print asterisks at the beginning and end, and spaces in between
            print('*' + ' ' * (n - 2) + '*')

# Example usage:
size = 5
print_hollow_square(size)

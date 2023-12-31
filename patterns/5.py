def print_hollow_pyramid(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print(' ' * (n - i) + '*' * (2 * i - 1))
        else:
            print(' ' * (n - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')

# Example usage:
height = 5
print_hollow_pyramid(height)

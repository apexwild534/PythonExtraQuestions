def generate_spiral_pattern(n):
    spiral = [[0] * n for _ in range(n)]
    num = 1

    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            spiral[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            spiral[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            spiral[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            spiral[i][left] = num
            num += 1
        left += 1

    return spiral

# Example usage:
n = 4
spiral_pattern = generate_spiral_pattern(n)

for row in spiral_pattern:
    for num in row:
        print(f'{num:2d}', end=' ')
    print()

def generate_pascals_triangle(n):
    triangle = []

    for line in range(1, n + 1):
        row = []
        for i in range(line):
            if i == 0 or i == line - 1:
                row.append(1)
            else:
                prev_row = triangle[-1]
                row.append(prev_row[i - 1] + prev_row[i])
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        formatted_row = ' '.join(map(str, row))
        print(f"{formatted_row:^{max_width}}")

# Example usage:
n = 5
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)

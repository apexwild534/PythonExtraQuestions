def dot_product(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length for dot product calculation.")

    result = sum(x * y for x, y in zip(tuple1, tuple2))
    return result

# Example usage:
tuple1 = (2, 3, 5)
tuple2 = (4, 1, 6)
result = dot_product(tuple1, tuple2)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Dot product:", result)

def rotate_left(input_list, positions):
    if positions < 0:
        return input_list  # No rotation needed for negative positions
    n = len(input_list)
    positions = positions % n  # Handle positions greater than list length
    return input_list[positions:] + input_list[:positions]

# Example usage:
original_list = [1, 2, 3, 4, 5]
positions_to_rotate = 2

rotated_list = rotate_left(original_list, positions_to_rotate)
print("Original list:", original_list)
print(f"List rotated to the left by {positions_to_rotate} positions:", rotated_list)

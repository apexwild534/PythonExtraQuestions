def is_sorted_ascending(input_list):
    for i in range(1, len(input_list)):
        if input_list[i - 1] > input_list[i]:
            return False
    return True

# Example usage:
sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [3, 1, 4, 2, 5]

print("Is sorted_list sorted in ascending order?", is_sorted_ascending(sorted_list))
print("Is unsorted_list sorted in ascending order?", is_sorted_ascending(unsorted_list))

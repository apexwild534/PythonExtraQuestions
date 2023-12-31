def remove_duplicates_preserve_order(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 5]
result_list = remove_duplicates_preserve_order(original_list)

print("Original list:", original_list)
print("List with duplicates removed:", result_list)

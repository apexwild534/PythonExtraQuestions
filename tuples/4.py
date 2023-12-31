def sort_tuples_by_second_element(tuples_list):
    # Use the sorted() function with a custom key to sort the tuples
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
    return sorted_tuples

# Example usage:
tuples_list = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_list = sort_tuples_by_second_element(tuples_list)

print("Original list of tuples:", tuples_list)
print("Sorted list of tuples based on the second element:", sorted_list)

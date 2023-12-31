def merge_and_remove_duplicates(tuple1, tuple2):
    # Merge the two tuples
    merged_tuple = tuple1 + tuple2

    # Create a set to keep track of seen elements
    seen = set()
    
    # List to store unique elements while preserving order
    unique_elements = []

    # Iterate through the merged tuple
    for element in merged_tuple:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)

    # Convert the list back to a tuple
    result = tuple(unique_elements)
    return result

# Example usage:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
merged_result = merge_and_remove_duplicates(tuple1, tuple2)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Merged tuple with duplicates removed:", merged_result)

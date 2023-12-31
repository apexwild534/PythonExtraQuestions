def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range for the list."

# Test the function
print(get_element([1, 2, 3, 4, 5], 3)) # Output: 4
print(get_element([1, 2, 3, 4, 5], 10)) # Output: Error: Index 10 is out of range for the list.
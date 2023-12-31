def get_even_numbers(input_list):
    even_numbers = [x for x in input_list if x % 2 == 0]
    return even_numbers

# Example usage:
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = get_even_numbers(original_list)
print("Even numbers from the original list:", result_list)

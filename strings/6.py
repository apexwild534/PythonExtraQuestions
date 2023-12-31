def remove_vowels(input_string):
    vowels = "AEIOUaeiou"  # Define a string of vowels
    # Use a list comprehension to remove vowels
    filtered_string = ''.join([char for char in input_string if char not in vowels])
    return filtered_string

# Example usage:
input_string = "This is a sample string with some vowels."
result = remove_vowels(input_string)
print(result)

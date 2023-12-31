def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()
    reversed_string = input_string[::-1]
    return input_string == reversed_string

# Example usage:
test_string = "race car"
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")

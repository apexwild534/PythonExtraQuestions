def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

# Example usage:
string1 = "racecar"
string2 = "hello"

if is_palindrome(string1):
    print(f'"{string1}" is a palindrome.')
else:
    print(f'"{string1}" is not a palindrome.')

if is_palindrome(string2):
    print(f'"{string2}" is a palindrome.')
else:
    print(f'"{string2}" is not a palindrome.')

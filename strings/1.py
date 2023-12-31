def count_characters(input_string):
    # Remove spaces and tabs if needed
    input_string = input_string.replace(" ", "").replace("\t", "")
    character_count = len(input_string)
    return character_count

# Example usage:
input_string = "This is a sample string."
count = count_characters(input_string)
print(f"Total characters in the string: {count}")

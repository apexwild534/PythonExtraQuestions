def replace_text(file_name, output_file_name, target, replacement):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            modified_text = text.replace(target, replacement)
            with open(output_file_name, 'w') as output_file:
                output_file.write(modified_text)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

file_name = "sample4.txt"  # Replace with the actual file name
output_file_name = "modified_output.txt"  # Replace with the desired output file name
target_word = "old_word"
replacement_word = "new_word"
replace_text(file_name, output_file_name, target_word, replacement_word)
print(f"Text modified and saved to '{output_file_name}'")

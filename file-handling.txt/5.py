def add_line_numbers(file_name, output_file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            with open(output_file_name, 'w') as output_file:
                for i, line in enumerate(lines, 1):
                    output_file.write(f"Line {i}: {line}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

file_name = "sample5.txt"  # Replace with the actual file name
output_file_name = "output_with_line_numbers.txt"  # Replace with the desired output file name
add_line_numbers(file_name, output_file_name)
print(f"Line numbers added and saved to '{output_file_name}'")

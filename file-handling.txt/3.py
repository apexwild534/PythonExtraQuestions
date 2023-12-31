def reverse_lines(file_name, output_file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            reversed_lines = reversed(lines)
            with open(output_file_name, 'w') as output_file:
                for line in reversed_lines:
                    output_file.write(line)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

file_name = "input.txt"  # Replace with the actual file name
output_file_name = "reversed_output.txt"  # Replace with the desired output file name
reverse_lines(file_name, output_file_name)
print(f"Lines reversed and saved to '{output_file_name}'")

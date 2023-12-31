def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return f"Error: The file {file_path} does not exist."
    except PermissionError:
        return f"Error: You do not have permission to read the file {file_path}."

# Test the function
print(read_data('test.txt')) # Output: Error: The file test.txt does not exist.
print(read_data('/etc/passwd')) # Output: Error: You do not have permission to read the file /etc/passwd.
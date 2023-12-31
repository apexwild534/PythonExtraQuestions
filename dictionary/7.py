def extract_values(dict_list, key):
    return [d[key] for d in dict_list]

# Example usage:

dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

key = "name"

print(extract_values(dict_list, key)) # Output: ['Alice', 'Bob', 'Charlie']
person = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'occupation': 'Software Engineer',
    'hobbies': ['Reading', 'Traveling', 'Coding']
}

key_to_check = 'age'

if key_to_check in person:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
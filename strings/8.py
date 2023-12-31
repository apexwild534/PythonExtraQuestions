import random
import string

def generate_random_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by sampling from the character set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage:
password_length = 12
random_password = generate_random_password(password_length)
print("Random Password:", random_password)

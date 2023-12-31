def caesar_cipher(text, shift, mode):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == "encode":
                shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift_amount) % 26) + ord('a' if char.islower() else 'A'))
            elif mode == "decode":
                shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') - shift_amount) % 26) + ord('a' if char.islower() else 'A'))
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
input_text = "Hello, World!"
shift_value = 3
encrypted_text = caesar_cipher(input_text, shift_value, "encode")
print("Encoded:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift_value, "decode")
print("Decoded:", decrypted_text)

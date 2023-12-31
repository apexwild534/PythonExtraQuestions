def character_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            character_freq = {}
            for char in text:
                if char.isalpha():
                    char = char.lower()  # Convert to lowercase for case insensitivity
                    character_freq[char] = character_freq.get(char, 0) + 1
            sorted_freq = sorted(character_freq.items(), key=lambda x: x[1], reverse=True)
            return sorted_freq
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

file_name = "sample2.txt"  # Replace with the actual file name
char_freq = character_frequency(file_name)

if char_freq is not None:
    print("Character Frequency (Descending Order):")
    for char, freq in char_freq:
        print(f"'{char}': {freq} times")

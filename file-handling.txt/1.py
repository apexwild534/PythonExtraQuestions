def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

file_name = "sample1.txt"  # Replace with the actual file name
word_count = count_words_in_file(file_name)

if word_count is not None:
    print(f"Total number of words in '{file_name}': {word_count}")

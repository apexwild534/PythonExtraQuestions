def count_word_occurrence(text, target_word):
    # Split the text into words
    words = text.split()
    # Initialize a counter for the target word
    count = 0

    # Iterate through the words and count occurrences
    for word in words:
        if word == target_word:
            count += 1

    return count

# Example usage:
input_text = "This is a sample text. This text is for demonstration purposes."
word_to_find = "text"
occurrence_count = count_word_occurrence(input_text, word_to_find)
print(f"The word '{word_to_find}' appears {occurrence_count+1} times.")

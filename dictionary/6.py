def word_frequency(text):
    # Convert the text to lowercase and split it into words
    words = text.lower().split()

    # Create a dictionary to store the frequency of each word
    frequency = {}

    # Iterate over each word in the words list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            frequency[word] = 1

    # Return the dictionary of word frequencies
    return frequency

# Example usage:

text = "This is a sample text. This text is used to demonstrate the word frequency function."
print(word_frequency(text))
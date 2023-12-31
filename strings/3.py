def capitalize_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    capitalized_words = [word.capitalize() for word in words]  # Capitalize each word
    capitalized_sentence = ' '.join(capitalized_words)  # Join the words into a sentence
    return capitalized_sentence

# Example usage:
input_sentence = "this is a sample sentence."
capitalized = capitalize_sentence(input_sentence)
print(capitalized)

def replace_text(original_text, target_word, replacement_word):
    modified_text = original_text.replace(target_word, replacement_word)
    return modified_text

# Example usage:
input_text = "This is a sample sentence. It has the word 'sample' in it."
word_to_replace = "sample"
replacement_word = "example"
new_text = replace_text(input_text, word_to_replace, replacement_word)
print(new_text)

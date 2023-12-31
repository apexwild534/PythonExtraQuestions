python
def find_max_key(dictionary):
    if not dictionary:
        return None
    max_key = max(dictionary, key=dictionary.get)
    return max_key

# Example usage:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

print(find_max_key(dict1)) # Output: 'c'
print(find_max_key(dict2)) # Output: 'f'
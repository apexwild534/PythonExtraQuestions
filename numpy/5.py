import numpy as np

def normalize_array(input_array):
    min_val = np.min(input_array)
    max_val = np.max(input_array)
    normalized_array = (input_array - min_val) / (max_val - min_val)
    return normalized_array

# Example usage:
input_array = np.array([1, 2, 3, 4, 5])

normalized = normalize_array(input_array)
print("Original array:", input_array)
print("Normalized array:", normalized)

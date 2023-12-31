import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Calculate the dot product using numpy.dot()
dot_product1 = np.dot(array1, array2)

# Calculate the dot product using the @ operator (Python 3.5+)
dot_product2 = array1 @ array2

# Print the results
print("Array 1:", array1)
print("Array 2:", array2)
print("Dot Product (using numpy.dot()):", dot_product1)
print("Dot Product (using @ operator):", dot_product2)

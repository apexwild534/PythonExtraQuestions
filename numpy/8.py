import numpy as np

def find_eigenvalues_and_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage:
square_matrix = np.array([[4, -2],
                         [1,  1]])

eigenvalues, eigenvectors = find_eigenvalues_and_eigenvectors(square_matrix)

print("Matrix:")
print(square_matrix)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

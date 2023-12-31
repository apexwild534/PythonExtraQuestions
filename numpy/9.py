import numpy as np

def calculate_svd(matrix):
    U, S, VT = np.linalg.svd(matrix)
    return U, S, VT

# Example usage:
matrix = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

U, S, VT = calculate_svd(matrix)

print("Original Matrix:")
print(matrix)

print("U (Left Singular Vectors):")
print(U)

print("S (Singular Values):")
print(S)

print("VT (Right Singular Vectors Transpose):")
print(VT)

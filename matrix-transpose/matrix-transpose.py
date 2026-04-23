import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    shape = A.shape
    transpose_matrix = [[0]*shape[0] for _ in range(shape[1])]
    for i in range(shape[0]):
        for j in range(shape[1]):
            transpose_matrix[j][i] = A[i][j]

    return np.array(transpose_matrix)
            


import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A = np.array(A, dtype=float)
    n = A.shape[0]

    aug = np.hstack((A, np.eye(n)))

    for col in range(n):
        pivot_row = col + np.argmax(np.abs(aug[col:, col]))

        if np.isclose(aug[pivot_row,col],0):
            return None

        aug[[col, pivot_row]] = aug[[pivot_row,col]]

        aug[col] /= aug[col,col]

        for row in range(n):
            if row != col: 
                factor = aug[row,col]
                aug[row] -= factor * aug[col]

    return aug[:,n:]
    
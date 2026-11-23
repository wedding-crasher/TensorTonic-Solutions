import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.array(X,dtype = float)
    centered = X - X.mean( axis = 0)

    covariance = centered.T @ centered / len(X)

    print(covariance)
    # Find Eigenvalues 

    w, V = np.linalg.eig(covariance)

    idx = np.argsort(w)[::-1]

    V_top = V[:, idx[:k]]

    
    X_proj = centered @ V_top
    return X_proj
    
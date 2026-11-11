import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    np_X = np.array(X)
    shifted_X = np.array([ vector - np_X.mean(axis = 0 ) for vector in np_X])
    
    covariance_matrix = (shifted_X.T @ shifted_X) / (shifted_X.shape[0] -1)
    return covariance_matrix
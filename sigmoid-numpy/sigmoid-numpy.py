import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    vec = np.array(x)
    output = 1 / (1 + np.exp(-vec))
    return output
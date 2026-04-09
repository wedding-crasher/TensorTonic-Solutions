import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    output = []
    for num in x:
        if num > 0: 
            output.append(num)
        else: 
            output.append(alpha * num)
    return np.array(output)
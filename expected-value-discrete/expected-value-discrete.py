import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code her 
    
    x = np.array(x)
    p = np.array(p)

    if sum(p) != 1:
        raise ValueError
    

    output = sum(x * p)
    
    return output

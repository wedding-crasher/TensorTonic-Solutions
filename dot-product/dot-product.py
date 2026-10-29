import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    sum = 0 
    for x,y in zip(x,y):
        sum += x*y 

    return float(sum)
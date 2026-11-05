import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    list = np.array(x)
    pmf = np.array([ p if num == 1 else 1 - p for num in list ])
    
    return {"pmf" : pmf, "mean": float(p) , "variance" : float(p*(1-p))}
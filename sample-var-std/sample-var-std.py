import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    list_np = np.array(x)
    mean = list_np.mean()

    variance = sum((list_np - mean)**2)/(len(list_np)-1)
    standard_deviation = variance ** (1/2)
    return {"variance": float(variance), "standard_deviation":float(standard_deviation)}
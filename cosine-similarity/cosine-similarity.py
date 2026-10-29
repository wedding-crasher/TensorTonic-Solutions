import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    dotproduct = a @ b
    a_norm = (a @ a)**(1/2)
    b_norm = (b@b)**(1/2)

    if a_norm == 0 or b_norm == 0 : 
        return float(0)
    else :
        return float( dotproduct / (a_norm * b_norm))


    
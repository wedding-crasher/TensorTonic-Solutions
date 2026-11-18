import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.array(x)

    std = math.sqrt(np.sum((x - x.mean())** 2) /(len(x)  - 1))
    t = (x.mean() - mu0) / (std / math.sqrt(len(x)))
    return float(t)
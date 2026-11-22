import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    rng = np.random.default_rng(seed)
    samples_mean = []
    for i in range(n_bootstrap):
        sample = rng.choice(x, size = len(x), replace = True)
        samples_mean.append(sample.mean())
    samples_mean = np.array(samples_mean)

    a = (1-ci) / 2
    lower, upper = np.quantile(samples_mean, [a, 1-a])
    return {"bootstrap_mean": samples_mean.mean(), "lower": lower, "upper": upper } 
        
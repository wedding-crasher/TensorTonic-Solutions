import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf = ((math.e)**(-lam)) * (lam ** k) / math.factorial(k)

    cmf = sum([((math.e)**(-lam)) * (lam ** k) / math.factorial(k) for k in range(k + 1)])

    return { "pmf" : pmf, "cdf": cmf}
import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    # Pmf 
   

    pmf = math.comb(n,k)*(p ** k)*((1-p)**(n-k))

    cmf = sum([  math.comb(n,k)*(p ** k)*((1-p)**(n-k)) for k in range(k + 1)])

    return { "pmf" : float(pmf), "cdf": float(cmf)}
from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = sum(x) / len(x)


    sorted_x = sorted(x)
    median = sorted_x[len(x) // 2] if len(x) % 2 == 1 else ((sorted_x[len(x)//2 - 1]) +(sorted_x[len(x)//2 ])) / 2
    
    counter = Counter(x)
    max_frequency = counter.most_common(1)[0][1]
    mode = []
    for i ,f in counter.items() : 
        if f == max_frequency:
            mode.append(float(i))

   
    mode = sorted(mode)[0]
    return {"mean" : float(mean), "median" : float(median), "mode" : mode  }
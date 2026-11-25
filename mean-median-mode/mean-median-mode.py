from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    count = Counter(x)
    mode = min(i for i , k in count.items() if k == max(count.values()))
    return  {f"mean" : float(mean), "median" :float(median) , "mode": float(mode)}
    
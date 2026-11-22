import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    a = np.array(A)
    row , col = np.shape(a)
    res = np.zeros((col , row) , dtype = a.dtype )

    for i in range(row):
        for j in range(col):
            res[j][i] = a[i][j]
    return res
        
    
        
    

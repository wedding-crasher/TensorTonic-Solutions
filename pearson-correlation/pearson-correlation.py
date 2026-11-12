import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    # Covariance Matrix 부터 
    # Centering 부터 하자 
    X = np.array(X)
    centered = X - X.mean(axis = 0)
    print(centered)
    
    # 그 다음 
    covariance_m = (centered.T @ centered) / (centered.shape[0] -1)

    # 표준 편차 계산 
    std = np.sqrt(np.sum((centered ** 2),axis = 0)/(centered.shape[0]-1))

        
    for row in range(covariance_m.shape[0]):
        for col in range(covariance_m.shape[1]):
            covariance_m[row][col] = covariance_m[row][col] / (std[row] * std [col])

    return covariance_m
                
        
    
    
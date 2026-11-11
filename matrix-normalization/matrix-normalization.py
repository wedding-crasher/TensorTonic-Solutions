import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix = np.array(matrix, dtype = "float")
    if axis == 0:
        if norm_type == "l1":
            normed_matrix = matrix / matrix.sum(axis =0)
            return normed_matrix

        elif norm_type == "l2":
            l2 = []
            for col in range(matrix.shape[1]):
                l2_norm_col = (sum([ (matrix[row][col])**2 for row in range(matrix.shape[0])]))**(1/2)
                l2.append(l2_norm_col)
            l2 = np.array(l2)
            normed_matrix = matrix / l2
            return normed_matrix
        else: 
            normed_matrix = matrix / matrix.max(axis = 0)
            return normed_matrix

    elif axis == 1:
        if norm_type == "l1":
            l1_norm = matrix.sum(axis = 1)
  
          
            normed_matrix = np.array( [matrix[row] / l1_norm[row] for row in range(matrix.shape[0])])
            return normed_matrix


        
        elif norm_type == "l2":
            l2 = []
            for row in range(matrix.shape[0]):
                l2_norm_row = sum([ (matrix[row][col])**2 for col in range(matrix.shape[1])])**(1/2)
                l2.append(l2_norm_row)

            l2 = np.array(l2)
            print(l2)
    
            normed_matrix = []
            for row in range(matrix.shape[0]):
                if l2[row] != 0: 
                    normed_row = matrix[row] / l2[row]
                else: 
                    normed_row = [ 0 for _ in range(matrix.shape[1])]
                
                normed_matrix.append(normed_row)
            
            return np.array(normed_matrix)

        else:
            max_norm = matrix.max(axis = 1)

          
            normed_matrix = np.array( [matrix[row] / max_norm[row] for row in range(matrix.shape[0])])
            
            return normed_matrix

    else:
        if norm_type == "l1":
            l1_norm = matrix.sum()
            return matrix / l1_norm


        
        elif norm_type == "l2":
            l2_norm = 0 
            for row in range(matrix.shape[0]):
                for col in range(matrix.shape[1]):
                    l2_norm += (matrix[row][col])**(2)
            l2_norm = l2_norm**(1/2)
            return matrix / l2_norm

        else:
            max_norm = matrix.max()
        
            
            return matrix / max_norm
        
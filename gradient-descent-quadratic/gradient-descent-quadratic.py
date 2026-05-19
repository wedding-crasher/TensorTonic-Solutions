def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    point = x0 

    for i in range(steps): 
        point = point - lr * (2 * a * point + b)
    
    return point 
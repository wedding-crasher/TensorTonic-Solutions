import numpy as np

# def leaky_relu(x, alpha=0.01):
#     """
#     Vectorized Leaky ReLU implementation.
#     """
#     # Write code here
#     output = []
#     for num in x:
#         if num > 0: 
#             output.append(num)
#         else: 
#             output.append(alpha * num)
#     return np.array(output)

# 위는 np 안쓰고, 쫒같이 짜건ㅅ

def leaky_relu(x, alpha= 0.01):
    vec = np.array(x, dtype=float)
    vec = np.where(vec >0, vec, vec*alpha)
    return vec
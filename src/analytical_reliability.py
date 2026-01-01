import numpy as np

def analytical_reliability(lambda_rate, t):
    return np.exp(-lambda_rate * t)

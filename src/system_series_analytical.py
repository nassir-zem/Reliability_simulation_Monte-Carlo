import numpy as np

def system_series_analytical(lambdas, t):
    """
    Fiabilité analytique d'un système en série
    """
    return np.exp(-sum(lambdas) * t)

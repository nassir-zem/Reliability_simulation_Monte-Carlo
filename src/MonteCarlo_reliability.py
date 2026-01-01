import numpy as np

def simulate_machine(lambda_rate, t, N=100000):
    lifetimes = np.random.exponential(1 / lambda_rate, N)
    reliability = np.mean(lifetimes > t)
    return reliability

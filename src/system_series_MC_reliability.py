from MonteCarlo_reliability import monte_carlo_reliability

def system_reliability(lambdas, t):
    R = 1
    for lam in lambdas:
        R *= monte_carlo_reliability(lam, t)
    return R

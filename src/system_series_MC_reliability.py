from monte_carlo import simulate_machine

def system_reliability(lambdas, t):
    R = 1
    for lam in lambdas:
        R *= simulate_machine(lam, t)
    return R

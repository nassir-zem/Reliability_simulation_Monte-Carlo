import numpy as np

def monte_carlo_reliability(lambda_, t, n_sim=10000):
    """
    Simulation Monte Carlo de la fiabilité
    lambda_ : taux de défaillance
    t : temps (heures)
    n_sim : nombre de simulations
    """
    # Générer des temps de défaillance (loi exponentielle)
    failure_times = np.random.exponential(scale=1/lambda_, size=n_sim)

    # Compter les machines encore en marche à t
    survivors = np.sum(failure_times > t)

    # Fiabilité estimée
    R_t = survivors / n_sim

    return R_t


# === TEST ===
if __name__ == "__main__":
    lambda_test = 0.002   # exemple
    t = 500               # heures

    R = monte_carlo_reliability(lambda_test, t)
    print("Fiabilité Monte Carlo à t={} h : {}".format(t, R))


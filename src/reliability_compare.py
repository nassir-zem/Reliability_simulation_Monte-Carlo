import numpy as np
import matplotlib.pyplot as plt

from MonteCarlo_reliability import monte_carlo_reliability
from analytical_reliability import analytical_reliability

# Paramètres
lambda_ = 0.002
t_values = np.linspace(0, 2000, 50)

R_mc = []
R_an = []

for t in t_values:
    R_mc.append(monte_carlo_reliability(lambda_, t, n_sim=50000))
    R_an.append(analytical_reliability(lambda_, t))

# Tracé
plt.figure()
plt.plot(t_values, R_mc, label="Monte Carlo")
plt.plot(t_values, R_an, label="Analytique")
plt.xlabel("Temps (heures)")
plt.ylabel("Fiabilité R(t)")
plt.title("Comparaison Fiabilité : Monte Carlo vs Analytique")
plt.legend()
plt.grid(True)
plt.show()

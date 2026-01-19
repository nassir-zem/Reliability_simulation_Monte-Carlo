import numpy as np
import matplotlib.pyplot as plt

from system_series_MC_reliability import system_reliability
from system_series_analytical import system_series_analytical

lambdas = [0.002, 0.0015, 0.001]
t_values = np.linspace(0, 2000, 40)

R_mc = []
R_an = []

for t in t_values:
    R_mc.append(system_reliability(lambdas, t))
    R_an.append(system_series_analytical(lambdas, t))

plt.figure()
plt.plot(t_values, R_mc, label="Monte Carlo")
plt.plot(t_values, R_an, label="Analytique")
plt.xlabel("Temps (heures)")
plt.ylabel("Fiabilité du système")
plt.title("Fiabilité d'un système en série")
plt.legend()
plt.grid(True)
plt.show()

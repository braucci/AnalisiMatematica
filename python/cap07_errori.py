"""
cap07_errori.py — codice del capitolo 7 (07-differenziabilita).
Eseguire dalla cartella Libro/:  python3 python/cap07_errori.py
"""
import numpy as np

R = 287.05
rho = lambda p, T: p / (R * T)           # densità dell'aria
p0, T0, dp, dT = 101325.0, 288.15, 300.0, 1.5   # misure e incertezze
r0 = rho(p0, T0)
lin = r0 * (dp / p0 + dT / T0)           # stima con il differenziale
rng = np.random.default_rng(1)
p = p0 + rng.uniform(-dp, dp, 100000)
T = T0 + rng.uniform(-dT, dT, 100000)
print(f"rho = {r0:.5f} kg/m^3")
print(f"errore massimo (differenziale): {lin:.5f}"
      f"  ({lin / r0:.2%})")
print(f"errore massimo osservato (simulazione): "
      f"{np.max(np.abs(rho(p, T) - r0)):.5f}")

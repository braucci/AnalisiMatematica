"""
cap11_glauert.py — codice del capitolo 11 (06-criteri).
Eseguire dalla cartella Libro/:  python3 python/cap11_glauert.py
"""
import numpy as np

AR, N = 6.0, 12                    # allungamento, termini (dispari)
n = np.arange(1, 2 * N, 2)         # n = 1, 3, 5, ..., 23
th = np.arange(1, N + 1) * np.pi / (2 * N)   # stazioni in (0, pi/2]
mu = 2 * np.pi / (4 * AR)          # a0 c / (4 b), ala rettangolare
M = np.sin(np.outer(th, n)) * (np.sin(th)[:, None] + n * mu)
A = np.linalg.solve(M, mu * np.sin(th))     # incidenza di 1 rad
r = A / A[0]
termini = n[1:] * r[1:]**2
print("A_n/A_1 :", np.array2string(r[:5], precision=5))
print("delta_N :", np.array2string(np.cumsum(termini)[:5],
                                   precision=5))
print(f"delta = {termini.sum():.4f},  C_L/alpha = "
      f"{np.pi * AR * A[0]:.3f} /rad,  1/(1+delta) = "
      f"{1 / (1 + termini.sum()):.4f}")

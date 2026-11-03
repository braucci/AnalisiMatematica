"""
cap04_efficienza.py — codice del capitolo 4 (07-teoremi-continue).
Eseguire dalla cartella Libro/:  python3 python/cap04_efficienza.py
"""
import math

# Polare parabolica: C_D = C_D0 + k C_L^2, con k = 1/(pi e AR)
CD0, AR, e_osw, CLmax = 0.025, 8.0, 0.80, 1.4
k = 1 / (math.pi * e_osw * AR)
E = lambda CL: CL / (CD0 + k * CL**2)       # efficienza L/D

# Weierstrass: E è continua su [0, CLmax], quindi ha massimo.
# Lo cerchiamo su una griglia fitta e lo confrontiamo con la formula.
N = 140000
CL_griglia = max((CLmax * i / N for i in range(N + 1)), key=E)
CL_star = math.sqrt(CD0 / k)
print(f"k = {k:.5f}")
print(f"griglia:  C_L = {CL_griglia:.4f}   E = {E(CL_griglia):.4f}")
E_max = 1 / (2 * math.sqrt(CD0 * k))
print(f"formula:  C_L = {CL_star:.4f}   E = {E_max:.4f}")

"""
cap06_snell.py — codice del capitolo 6 (09-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap06_snell.py
"""
import math
from scipy.optimize import brentq

# raggio da A=(0, h1) a B=(L, -h2); velocità v1 sopra, v2 sotto
h1, h2, L, v1, v2 = 1.0, 1.0, 2.0, 1.0, 0.75
T = lambda x: math.hypot(h1, x) / v1 + math.hypot(h2, L - x) / v2
dT = lambda x: (x / math.hypot(h1, x) / v1
                - (L - x) / math.hypot(h2, L - x) / v2)
xs = brentq(dT, 0, L)                    # T'(x) = 0, unico zero
s1, s2 = xs / math.hypot(h1, xs), (L - xs) / math.hypot(h2, L - xs)
print(f"x* = {xs:.6f}   T(x*) = {T(xs):.6f}")
print(f"sen t1 / v1 = {s1 / v1:.6f}   sen t2 / v2 = {s2 / v2:.6f}")
print(f"T(0) = {T(0):.6f}   T(L) = {T(L):.6f}")

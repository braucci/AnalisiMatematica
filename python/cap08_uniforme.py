"""
cap08_uniforme.py — codice del capitolo 8 (05-uniforme-continuita).
Eseguire dalla cartella Libro/:  python3 python/cap08_uniforme.py
"""
import math

eps = 0.1
print("f(x) = x^2: delta massimo in x0, eps = 0.1")
for x0 in (0, 1, 10, 100, 1000):
    d = math.sqrt(x0**2 + eps) - x0            # formula (delta-x2)
    print(f"   x0 = {x0:7.2f}:  delta = {d:.3e}")
print("f(x) = sqrt(x): delta massimo in x0, eps = 0.1")
for x0 in (0, 0.0025, 1, 100, 1000):
    r = math.sqrt(x0)
    # a destra: (r + eps)^2 - x0;  a sinistra: x0 - (r - eps)^2
    d = 2 * eps * r + eps**2 if r < eps else 2 * eps * r - eps**2
    print(f"   x0 = {x0:7.4g}:  delta = {d:.3e}")

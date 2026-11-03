"""
cap10_limiti_taylor.py — codice del capitolo 10 (02-o-piccoli).
Eseguire dalla cartella Libro/:  python3 python/cap10_limiti_taylor.py
"""
import math
import sympy as sp
from mpmath import mp, mpf, sin as msin

x = sp.symbols('x')
f = 1 / x**2 - 1 / (x * sp.sin(x))
print(sp.series(f, x, 0, 4))
g = 1 / x - sp.cos(x) / x**3 + sp.sin(3 * x) / (3 * x**4)
print(sp.series(g, x, 0, 3))
print(sp.limit(sp.cos(x)**(-1 / x**2), x, 0))

mp.dps = 40                         # 40 cifre: valore "esatto"
print("     x      formula diretta      Taylor       esatto")
for k in (1, 3, 5, 7, 8):
    t = 10.0**(-k)
    d = 1 / t**2 - 1 / (t * math.sin(t))
    p = -1 / 6 - 7 * t**2 / 360
    e = 1 / mpf(t)**2 - 1 / (mpf(t) * msin(mpf(t)))
    print(f"  1e-{k}  {d:17.12f}  {p:14.12f}  {float(e):14.12f}")

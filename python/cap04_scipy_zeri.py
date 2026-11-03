"""
cap04_scipy_zeri.py — codice del capitolo 4 (08-bisezione).
Eseguire dalla cartella Libro/:  python3 python/cap04_scipy_zeri.py
"""
import math
from scipy.optimize import bisect, brentq

f = lambda x: math.exp(x) + x

# entrambe vogliono [a, b] con f(a), f(b) di segno discorde
x_b, info_b = bisect(f, -1, 0, xtol=1e-14, full_output=True)
x_r, info_r = brentq(f, -1, 0, xtol=1e-14, full_output=True)
print(f"bisect: {x_b:.14f}  ({info_b.iterations} iterazioni)")
print(f"brentq: {x_r:.14f}  ({info_r.iterations} iterazioni)")
try:
    bisect(f, 0, 1)            # f(0) = 1, f(1) = e + 1: stesso segno
except ValueError as err:
    print("errore:", err)

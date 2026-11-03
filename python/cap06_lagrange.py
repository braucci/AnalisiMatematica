"""
cap06_lagrange.py — codice del capitolo 6 (02-rolle-lagrange).
Eseguire dalla cartella Libro/:  python3 python/cap06_lagrange.py
"""
import math
from scipy.optimize import brentq

def xi_lagrange(f, df, a, b):
    """Un punto xi in (a, b) con f'(xi) = [f(b) - f(a)] / (b - a)."""
    m = (f(b) - f(a)) / (b - a)          # pendenza della corda
    return brentq(lambda t: df(t) - m, a + 1e-12, b - 1e-12), m

xi, m = xi_lagrange(lambda t: t**3, lambda t: 3 * t**2, 0, 2)
print(f"x^3:   corda = {m:.4f}   xi = {xi:.6f}"
      f"   2/sqrt(3)    = {2 / math.sqrt(3):.6f}")
xi, m = xi_lagrange(math.sin, math.cos, 0, math.pi / 2)
print(f"sen x: corda = {m:.4f}   xi = {xi:.6f}"
      f"   arccos(2/pi) = {math.acos(2 / math.pi):.6f}")

# stima di sqrt(101) con il teorema di Lagrange (vedi il testo)
sup = 10 + 1 / 20
inf = 10 + 1 / (2 * sup)
print(f"{inf:.6f} < sqrt(101) = {math.sqrt(101):.6f} < {sup:.6f}")

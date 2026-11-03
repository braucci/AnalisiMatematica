"""
cap10_arctg.py — codice del capitolo 10 (01-peano).
Eseguire dalla cartella Libro/:  python3 python/cap10_arctg.py
"""
from fractions import Fraction as F
import math

def arctg(x, n):
    """T(x) = x - x^3/3 + ... + (-1)^n x^(2n+1)/(2n+1)."""
    return sum((-1)**k * x**(2*k + 1) / (2*k + 1)
               for k in range(n + 1))

for n in (10, 100, 1000):
    print(f"Leibniz, n = {n:4d}:  4*T = {4 * arctg(1.0, n):.10f}")
for n in (2, 4, 6, 8):
    p = 4 * (4 * arctg(F(1, 5), n) - arctg(F(1, 239), n))
    print(f"Machin,  n = {n}:     4*T = {float(p):.15f}")
print(f"                  pi    = {math.pi:.15f}")

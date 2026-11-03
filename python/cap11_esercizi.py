"""
cap11_esercizi.py — codice del capitolo 11 (10-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap11_esercizi.py
"""
import math
import sympy as sp

k = sp.symbols('k', integer=True, positive=True)
print(sp.summation(1 / (k * (k + 2)), (k, 1, sp.oo)))
print(sp.summation((2**k + 3**k) / 6**k, (k, 1, sp.oo)))
print(sp.summation(k / sp.factorial(k), (k, 1, sp.oo)),
      sp.summation(k**2 / sp.factorial(k), (k, 1, sp.oo)))
s3 = sp.summation((-1)**(k - 1) / k**3, (k, 1, sp.oo))
print(s3, "=", sp.N(s3, 8))
s9 = sum((-1)**(j - 1) / j**3 for j in range(1, 10))
print(f"s_9 = {s9:.6f}")
n = next(n for n in range(1, 1000) if 1 / (2 * n**2) < 1e-4)
print("termini per 1/k^3 con errore < 1e-4:", n)
r, t0 = 0.64, math.sqrt(2 / 9.81)
print(f"rimbalzi: spazio {(1+r)/(1-r):.2f} m, durata "
      f"{t0 * (1 + math.sqrt(r)) / (1 - math.sqrt(r)):.2f} s")

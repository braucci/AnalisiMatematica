"""
cap11_criteri.py — codice del capitolo 11 (06-criteri).
Eseguire dalla cartella Libro/:  python3 python/cap11_criteri.py
"""
import math
import sympy as sp

k, n = sp.symbols('k n', positive=True, integer=True)
print(sp.summation(1 / k**2, (k, 1, sp.oo)))           # Eulero
print(sp.summation(1 / (k * (k + 1)), (k, 1, sp.oo)))  # Mengoli
print(sp.limit(n**4 * (2*n + 1) / (n**5 + 4*n + 3), n, sp.oo))
print(sp.limit(n**2 * (1 - sp.cos(1 / n)), n, sp.oo))
a = sp.factorial(n) / n**n
print(sp.limit(sp.simplify(a.subs(n, n + 1) / a), n, sp.oo))

s = sum(math.factorial(j) / j**j for j in range(1, 60))
print(f"somma di k!/k^k (59 termini) = {s:.10f}")

"""
cap03_quoziente_polinomi.py — codice del capitolo 3 (03-limitate-operazioni).
Eseguire dalla cartella Libro/:  python3 python/cap03_quoziente_polinomi.py
"""
import sympy as sp

n = sp.symbols("n", positive=True, integer=True)
a = (n**2 + 5*n - 4) / (3*n**2 + 1)
print(sp.limit(a, n, sp.oo))           # calcolo simbolico del limite

# Controllo numerico: la distanza dal limite 1/3 si riduce come 1/n
terzo = sp.Rational(1, 3)
for k in [10, 100, 1000, 10**4]:
    v = a.subs(n, k)
    print(f"n = {k:>5d}:  a_n = {float(v):.8f},"
          f"  |a_n - 1/3| = {float(abs(v - terzo)):.2e}")

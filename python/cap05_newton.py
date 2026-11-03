"""
cap05_newton.py — codice del capitolo 5 (08-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap05_newton.py
"""
import math

def newton(f, df, x, passi):
    """Sostituisce x con lo zero della tangente in (x, f(x))."""
    for n in range(1, passi + 1):
        x = x - f(x) / df(x)
        print(f"  x_{n} = {x:.15f}   f(x_{n}) = {f(x):+.2e}")
    return x

print("x^3 + x - 1 = 0, partendo da x_0 = 1:")
newton(lambda x: x**3 + x - 1, lambda x: 3 * x**2 + 1, 1.0, 5)
e, M = 0.5, 1.0
print("Keplero E - e sen E = M (e = 0.5, M = 1), da E_0 = M:")
newton(lambda E: E - e * math.sin(E) - M,
       lambda E: 1 - e * math.cos(E), M, 4)

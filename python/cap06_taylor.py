"""
cap06_taylor.py — codice del capitolo 6 (07-taylor).
Eseguire dalla cartella Libro/:  python3 python/cap06_taylor.py
"""
import sympy as sp

x, b = sp.symbols("x b", real=True)
for f in (sp.exp(x), sp.log(1 + x), sp.sin(x), sp.cos(x)):
    print(f"{str(f):>10} =", sp.series(f, x, 0, 6))
print("  (1+x)**b =", sp.series((1 + x)**b, x, 0, 3))
print("  e^(-x^2) =", sp.series(sp.exp(-x**2), x, 0, 6))

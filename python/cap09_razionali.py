"""
cap09_razionali.py — codice del capitolo 9 (04-razionali).
Eseguire dalla cartella Libro/:  python3 python/cap09_razionali.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
q, r = sp.div(x**5 - 3*x**4 + x + 3, x**2 - 1, x)
print("quoziente:", q, "   resto:", r)
for f in [(x + 7) / (x**2 - x - 2), x / (x**2 + 2*x + 1),
          (1 - 2*x) / (x**2 + 2*x + 5),
          (x**5 - x + 1) / (x**4 + x**2)]:
    print("f =", f)
    print("    fratti semplici:", sp.apart(f, x))
    print("    integrale:      ", sp.integrate(f, x))

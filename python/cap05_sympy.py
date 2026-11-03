"""
cap05_sympy.py — codice del capitolo 5 (05-elementari).
Eseguire dalla cartella Libro/:  python3 python/cap05_sympy.py
"""
import sympy as sp

x = sp.symbols("x", positive=True)
funzioni = [x**3 * sp.sin(x), sp.sin(x**2), sp.sin(x)**2, sp.tan(x),
            sp.exp(x) / x, sp.log(x**2 + 1), x**x, sp.atan(1 / x)]
for f in funzioni:
    print(f"D[{f}] = {sp.simplify(sp.diff(f, x))}")

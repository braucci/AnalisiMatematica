"""
cap09_integrali_sympy.py — codice del capitolo 9 (03-integrale-indefinito).
Eseguire dalla cartella Libro/:  python3 python/cap09_integrali_sympy.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
esempi = [x / (x + 1), sp.tan(x)**2, sp.sin(x)**2, sp.tan(x),
          x * sp.exp(x**2), 1 / (x * sp.log(x))]
for f in esempi:
    F = sp.integrate(f, x)
    verifica = sp.simplify(sp.diff(F, x) - f)
    print(f"f = {f}")
    print(f"    F = {F}      F' - f = {verifica}")

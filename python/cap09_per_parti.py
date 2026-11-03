"""
cap09_per_parti.py — codice del capitolo 9 (05-per-parti).
Eseguire dalla cartella Libro/:  python3 python/cap09_per_parti.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
for f in [x * sp.cos(x), x**2 * sp.cos(x), sp.log(x), sp.atan(x),
          sp.exp(x) * sp.sin(x)]:
    F = sp.integrate(f, x)
    ok = sp.simplify(sp.diff(F, x) - f) == 0
    print(f"f = {f}:  F = {F}")
    print(f"    verifica F' = f: {ok}")
print("int_0^pi x sen x dx =",
      sp.integrate(x * sp.sin(x), (x, 0, sp.pi)))
print("int_1^e  log x dx   =", sp.integrate(sp.log(x), (x, 1, sp.E)))

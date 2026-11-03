"""
cap09_sostituzione.py — codice del capitolo 9 (06-sostituzione).
Eseguire dalla cartella Libro/:  python3 python/cap09_sostituzione.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
F = (sp.asin(x) + x * sp.sqrt(1 - x**2)) / 2       # formula trovata
d = sp.simplify(sp.diff(F, x) - sp.sqrt(1 - x**2))
print("F' - sqrt(1-x^2) =", d)
print("int_-1^1 sqrt(1-x^2) dx =",
      sp.integrate(sp.sqrt(1 - x**2), (x, -1, 1)))
t = sp.sqrt(2*x - 1)                                # esempio (b)
G = t**2 / 2 + 4*t + 8 * sp.log(sp.Abs(t - 1)) - 4 / (t - 1)
f = (x + sp.sqrt(2*x - 1)) / (x - sp.sqrt(2*x - 1))
for x0 in (sp.Rational(3, 4), 3, 7):
    d = sp.simplify(sp.diff(G, x).subs(x, x0) - f.subs(x, x0))
    print(f"x = {x0}:  G'(x) - f(x) = {sp.nsimplify(d)}")

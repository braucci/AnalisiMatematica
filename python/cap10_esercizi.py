"""
cap10_esercizi.py — codice del capitolo 10 (06-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap10_esercizi.py
"""
import math
import sympy as sp

x, M = sp.symbols('x M')
print(sp.series(sp.tan(x), x, 0, 7))
print(sp.series(sp.asin(x), x, 0, 7))
print(sp.diff(sp.sin(x**2), x, 10).subs(x, 0))
for e in (sp.log(1 + x) - sp.sin(x),
          sp.exp(x**2) - sp.cos(x) - sp.Rational(3, 2) * x**2,
          sp.tan(x) - sp.sin(x)):
    k = sp.Poly(sp.series(e, x, 0, 6).removeO(), x).monoms()[-1][0]
    print(f"limite = {sp.limit(e / x**k, x, 0)}  (ordine {k})")

R, s = 6371.0, 1000.0
print(f"arco - corda = {1000 * (s - 2*R*math.sin(s/(2*R))):.2f} m"
      f",  s^3/(24R^2) = {1000 * s**3 / (24 * R**2):.2f} m")

r = sp.Rational
esatto = ((1 + M**2 / 5)**r(7, 2) - 1) / (r(7, 10) * M**2)
print(sp.series(esatto, M, 0, 6))
for m in (0.1, 0.3, 0.5, 0.7):
    serie = 1 + m**2 / 4 + m**4 / 40
    print(f"M = {m}:  esatto {float(esatto.subs(M, m)):.5f}"
          f"   serie {serie:.5f}")

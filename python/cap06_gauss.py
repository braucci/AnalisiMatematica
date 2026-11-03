"""
cap06_gauss.py — codice del capitolo 6 (04-convessita).
Eseguire dalla cartella Libro/:  python3 python/cap06_gauss.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
f = sp.exp(-x**2)                       # curva di Gauss
d1 = sp.factor(sp.diff(f, x))
d2 = sp.factor(sp.diff(f, x, 2))
print("f'  =", d1)
print("f'' =", d2)
flessi = sorted(sp.solveset(d2, x, sp.S.Reals))
approx = [round(float(c), 4) for c in flessi]
print("f'' = 0 in", flessi, "~", approx)
for t in (-1, 0, 1):              # segno di f'' negli intervalli
    print(f"  f''({t}) = {d2.subs(x, t)}  ->",
          "convessa" if d2.subs(x, t) > 0 else "concava")
print("f(1/sqrt(2)) =", f.subs(x, flessi[1]),
      "~", round(float(f.subs(x, flessi[1])), 4))
print("punto critico x = 0:  f''(0) =",
      d2.subs(x, 0), "-> massimo relativo")

"""
cap06_gittata.py — codice del capitolo 6 (01-fermat).
Eseguire dalla cartella Libro/:  python3 python/cap06_gittata.py
"""
import sympy as sp

th, v, g = sp.symbols("theta v g", positive=True)
R = v**2 * sp.sin(2 * th) / g             # gittata nel vuoto
dR = sp.diff(R, th)
print("R'(theta) =", dR)
print("punti critici in (0, pi/2):",
      sp.solveset(dR, th, sp.Interval.open(0, sp.pi / 2)))
print("R'(0) =", dR.subs(th, 0),
      "   R'(pi/2) =", dR.subs(th, sp.pi / 2))
print("R(pi/4) =", R.subs(th, sp.pi / 4))

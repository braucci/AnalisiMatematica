"""
cap07_omogenee.py — codice del capitolo 7 (07-differenziabilita).
Eseguire dalla cartella Libro/:  python3 python/cap07_omogenee.py
"""
import sympy as sp

x, y = sp.symbols("x y", positive=True)
CL, AR, e = sp.symbols("C_L AR e", positive=True)
grado = lambda f, u, v: sp.simplify(       # per Eulero è il grado
    (u * sp.diff(f, u) + v * sp.diff(f, v)) / f)
for f in (x**2 + 3*x*y, sp.sqrt(x**2 + y**2), x*y / (x**2 + y**2),
          x / (x**2 + y**2)):
    print(f"f = {str(f):18}  (x f_x + y f_y)/f = {grado(f, x, y)}")
CDi = CL**2 / (sp.pi * e * AR)             # resistenza indotta
print("C_Di = C_L^2/(pi e AR): grado =", grado(CDi, CL, AR))

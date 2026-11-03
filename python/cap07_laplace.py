"""
cap07_laplace.py — codice del capitolo 7 (04-schwarz).
Eseguire dalla cartella Libro/:  python3 python/cap07_laplace.py
"""
import sympy as sp

x, y = sp.symbols("x y", real=True)
lap = lambda u: sp.simplify(sp.diff(u, x, 2) + sp.diff(u, y, 2))
for nome, phi in (("sorgente", sp.log(sp.sqrt(x**2 + y**2))),
                  ("vortice", sp.atan(y / x)),
                  ("doppietta", x / (x**2 + y**2)),
                  ("cilindro", x + x / (x**2 + y**2)),
                  ("non armonica", x**2 + y**2)):
    print(f"{nome:13} phi = {str(phi):24}  laplaciano = {lap(phi)}")

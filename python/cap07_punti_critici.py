"""
cap07_punti_critici.py — codice del capitolo 7 (05-massimi-minimi).
Eseguire dalla cartella Libro/:  python3 python/cap07_punti_critici.py
"""
import sympy as sp

x, y = sp.symbols("x y", real=True)

def classifica(f):
    """Punti critici di f(x, y) e loro natura con l'hessiano."""
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    H = sp.hessian(f, (x, y))
    for P in sp.solve([fx, fy], [x, y], dict=True):
        h = sp.simplify(H.det().subs(P))
        fxx = sp.simplify(H[0, 0].subs(P))
        if h > 0:
            tipo = "minimo" if fxx > 0 else "massimo"
        elif h < 0:
            tipo = "sella"
        else:
            tipo = "H = 0: il criterio non decide"
        print(f"({P[x]}, {P[y]}): H = {h}, f_xx = {fxx} -> {tipo}")

for f in (x**2 + y**2, y**2 - x**2, x**3 - 6*y*(x + y),
          y * sp.exp(-(x**2 + y**2)), x**3 + y**3 - 3*x*y):
    print("f =", f)
    classifica(f)

"""
cap07_tre_variabili.py — codice del capitolo 7 (06-piu-variabili).
Eseguire dalla cartella Libro/:  python3 python/cap07_tre_variabili.py
"""
import itertools
import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
f = x**2 + y**2 + z**2 + x*y*z
grad = [sp.diff(f, v) for v in (x, y, z)]
H = sp.hessian(f, (x, y, z))
print("grad f =", grad)
# direzioni di prova v; la derivata seconda lungo v è v^T H v
dirs = [sp.Matrix(v) for v in itertools.product((-1, 0, 1), repeat=3)
        if any(v)]
for P in sp.solve(grad, [x, y, z], dict=True):
    q = [int((v.T * H.subs(P) * v)[0]) for v in dirs]
    c = ", ".join(f"{int(P[s]):2d}" for s in (x, y, z))
    print(f"P = ({c}):  min v^T H v = {min(q):2d},"
          f"  max v^T H v = {max(q)}")

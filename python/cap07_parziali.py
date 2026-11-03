"""
cap07_parziali.py — codice del capitolo 7 (03-derivate-parziali).
Eseguire dalla cartella Libro/:  python3 python/cap07_parziali.py
"""
import sympy as sp

x, y = sp.symbols("x y", real=True)
for f in (x**2 + x*y**2, sp.sin(x*y), sp.exp(x), x + 2*y):
    gx, gy = sp.diff(f, x), sp.diff(f, y)
    print(f"f = {str(f):13}  f_x = {str(gx):10}  f_y = {gy}")

# controllo numerico con i rapporti incrementali, nel punto (1, 2)
F = sp.lambdify((x, y), x**2 + x*y**2)
h = 1e-6
print("f_x(1,2) ~", round((F(1 + h, 2) - F(1, 2)) / h, 4),
      "  f_y(1,2) ~", round((F(1, 2 + h) - F(1, 2)) / h, 4))

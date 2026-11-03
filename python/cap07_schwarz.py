"""
cap07_schwarz.py — codice del capitolo 7 (04-schwarz).
Eseguire dalla cartella Libro/:  python3 python/cap07_schwarz.py
"""
import sympy as sp

x, y, h = sp.symbols("x y h", real=True)
f = x**y                                 # definita per x > 0
fxy = sp.diff(f, x, y)              # prima rispetto a x, poi a y
fyx = sp.diff(f, y, x)              # prima rispetto a y, poi a x
print("f_xy =", sp.simplify(fxy), "   f_yx =", sp.simplify(fyx))
print("f_xy - f_yx =", sp.simplify(fxy - fyx))

# il controesempio: g = x^3 y / (x^2 + y^2), g(0, 0) = 0
g = x**3 * y / (x**2 + y**2)
gx0y = sp.simplify(sp.diff(g, x).subs(x, 0))   # g_x(0, y), y != 0
gyx0 = sp.simplify(sp.diff(g, y).subs(y, 0))   # g_y(x, 0), x != 0
print("g_x(0, y) =", gx0y, "   g_y(x, 0) =", gyx0)
# g_x(0,0) = g_y(0,0) = 0 (g è nulla sugli assi), quindi:
print("g_xy(0,0) =", sp.limit(gx0y.subs(y, h) / h, h, 0),
      "   g_yx(0,0) =", sp.limit(gyx0.subs(x, h) / h, h, 0))

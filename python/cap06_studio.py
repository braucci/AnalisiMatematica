"""
cap06_studio.py — codice del capitolo 6 (06-studio).
Eseguire dalla cartella Libro/:  python3 python/cap06_studio.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
f = x * sp.exp(1 / x)
print("limiti:", [sp.limit(f, x, p, d) for p, d in
                  ((-sp.oo, "+"), (0, "-"), (0, "+"), (sp.oo, "-"))])
d1 = sp.factor(sp.diff(f, x))
d2 = sp.factor(sp.diff(f, x, 2))
print("f'  =", d1, "   f' = 0 in", sp.solve(d1, x))
print("f'' =", d2)
print("f(1) =", f.subs(x, 1), "   f''(1) =", d2.subs(x, 1))
for p in (sp.oo, -sp.oo):                  # asintoti obliqui
    m = sp.limit(f / x, x, p)
    q = sp.limit(f - m * x, x, p)
    print(f"x -> {p}:  m = {m},  q = {q}")

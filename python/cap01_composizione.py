"""
cap01_composizione.py — codice del capitolo 1 (06-invertibili).
Eseguire dalla cartella Libro/:  python3 python/cap01_composizione.py
"""
# sympy manipola le espressioni simbolicamente, come faremmo a mano.
import sympy as sp
x, y = sp.symbols("x y", real=True)

g = 2*x + 1
f = sp.sqrt(x)
print("f(g(x)) =", f.subs(x, g))         # composizione f o g
print("g(f(x)) =", g.subs(x, f))         # composizione g o f

# Inversa di g: risolviamo y = g(x) rispetto a x
inversa = sp.solve(sp.Eq(y, g), x)[0]
print("g^-1(y) =", inversa)
# Verifica delle relazioni g^-1(g(x)) = x e g(g^-1(y)) = y
print(sp.simplify(inversa.subs(y, g)),
      sp.simplify(g.subs(x, inversa)))

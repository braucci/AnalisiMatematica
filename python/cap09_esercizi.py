"""
cap09_esercizi.py — codice del capitolo 9 (10-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap09_esercizi.py
"""
import sympy as sp

x, t = sp.symbols("x t", real=True)
G = sp.integrate(sp.exp(-t**2), (t, x, x**2))
print("G'(x) =", sp.simplify(sp.diff(G, x)))
lim = sp.limit(sp.integrate(sp.sin(t**2), (t, 0, x)) / x**3, x, 0)
print("lim =", sp.gammasimp(lim))
print("int x^2 e^x =", sp.factor(sp.integrate(x**2 * sp.exp(x), x)))
I = [sp.integrate(sp.sin(x)**n, (x, 0, sp.pi / 2)) for n in range(5)]
print("I_0..I_4 =", I)
print("int_0^oo x e^-x =",
      sp.integrate(x * sp.exp(-x), (x, 0, sp.oo)))
print("int_2^oo 1/(x log^2 x) =",
      sp.integrate(1 / (x * sp.log(x)**2), (x, 2, sp.oo)))

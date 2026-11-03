"""
cap07_edp.py — codice del capitolo 7 (04-schwarz).
Eseguire dalla cartella Libro/:  python3 python/cap07_edp.py
"""
import math
import sympy as sp

x, y, t, n = sp.symbols("x y t n", real=True)
k, c, M = sp.symbols("k c M", positive=True)
F, G, d = sp.Function("F"), sp.Function("G"), sp.diff
onde = lambda u: sp.simplify(d(u, t, 2) - c**2 * d(u, x, 2))
calore = lambda u: sp.simplify(d(u, t) - k * d(u, x, 2))
print("u_tt - c^2 u_xx per F(x-ct)+G(x+ct):",
      onde(F(x - c*t) + G(x + c*t)))
print("u_t - k u_xx per e^(-kn^2 t)sen(nx):",
      calore(sp.exp(-k * n**2 * t) * sp.sin(n*x)))
gauss = sp.exp(-x**2 / (4*k*t)) / sp.sqrt(4 * sp.pi * k * t)
print("u_t - k u_xx per la gaussiana:      ", calore(gauss))
# onde di Mach: (M^2 - 1) phi_xx - phi_yy = 0 per phi = F(x - beta y)
beta = sp.sqrt(M**2 - 1)
phi = F(x - beta * y)
print("(M^2-1) phi_xx - phi_yy:",
      sp.simplify((M**2 - 1) * d(phi, x, 2) - d(phi, y, 2)))
for Mach in (1.2, 1.5, 2.0, 3.0):
    mu = math.degrees(math.asin(1 / Mach))
    print(f"M = {Mach:.1f}:  angolo di Mach = {mu:5.2f} gradi")

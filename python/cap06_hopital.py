"""
cap06_hopital.py — codice del capitolo 6 (05-hopital).
Eseguire dalla cartella Libro/:  python3 python/cap06_hopital.py
"""
import sympy as sp

x = sp.symbols("x", real=True)
b = sp.Rational(1, 2)                    # un esponente positivo
esempi = [((sp.exp(x) - 1) / sp.sin(2*x), 0, "+-"),
          ((x**2 - 1) / sp.log(x), 1, "+-"),
          (sp.log(x) / x**b, sp.oo, "-"),
          (x**5 / sp.exp(x), sp.oo, "-"),
          (x**b * sp.log(x), 0, "+"),
          (1 / sp.sin(x) - 1 / x, 0, "+-"),
          (x**x, 0, "+"),
          ((1 + sp.sin(x))**(1/x), 0, "+-"),
          (x**(1/x), sp.oo, "-")]
for f, x0, verso in esempi:
    print(f"lim {str(f):>24} per x -> {x0}:",
          sp.limit(f, x, x0, verso))

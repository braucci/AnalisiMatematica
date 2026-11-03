"""
cap05_tasso.py — codice del capitolo 5 (01-tasso).
Eseguire dalla cartella Libro/:  python3 python/cap05_tasso.py
"""
from fractions import Fraction as F

p = lambda t: t**2                    # peso in funzione del tempo
t = F(10)
for k in range(0, 7):
    h = F(1, 10**k)                   # aritmetica razionale esatta
    tasso_medio = (p(t + h) - p(t)) / h
    print(f"h = {str(h):>9}   tasso medio = {float(tasso_medio)}")
print("previsione lineare p(11) ~", p(t) + 2 * t * 1,
      "  valore vero:", p(t + 1))

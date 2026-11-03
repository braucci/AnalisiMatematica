"""
cap08_esaustione.py — codice del capitolo 8 (01-esaustione).
Eseguire dalla cartella Libro/:  python3 python/cap08_esaustione.py
"""
from fractions import Fraction as F

def somme(n, b=F(1)):
    """Somme inferiore e superiore di x^2 in [0, b], n intervalli."""
    x = [F(k, n) * b for k in range(n + 1)]
    s = sum(x[k - 1]**2 * (x[k] - x[k - 1]) for k in range(1, n + 1))
    S = sum(x[k]**2 * (x[k] - x[k - 1]) for k in range(1, n + 1))
    return s, S

print(f"{'n':>5} {'s_n':>10} {'S_n':>10} {'S_n - s_n':>10}")
for n in (1, 2, 5, 10, 100, 1000):
    s, S = somme(n)
    print(f"{n:5d} {float(s):10.6f} {float(S):10.6f}"
          f" {float(S - s):10.6f}")
s, S = somme(10)
print("n = 10, valori esatti:", s, "< 1/3 <", S)

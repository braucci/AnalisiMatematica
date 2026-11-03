"""
cap03_numero_e.py — codice del capitolo 3 (08-numero-e).
Eseguire dalla cartella Libro/:  python3 python/cap03_numero_e.py
"""
import math

for n in [10, 1000, 10**5, 10**7]:
    a = (1 + 1/n) ** n
    b = (1 + 1/n) ** (n + 1)
    print(f"n = {n:>8d}:  {a:.10f} < e < {b:.10f}"
          f"   (ampiezza {b - a:.1e})")
print(f"math.e        = {math.e:.10f}")

# Insidia della virgola mobile: per n enorme 1 + 1/n si arrotonda.
# Confrontiamo il calcolo "ingenuo" con quello basato su log1p.
for k in [9, 12, 15, 16]:
    n = 10**k
    ingenuo = (1 + 1/n) ** n
    accurato = math.exp(n * math.log1p(1/n))
    print(f"n = 1e{k}:  ingenuo = {ingenuo:.10f}"
          f"   con log1p = {accurato:.10f}")

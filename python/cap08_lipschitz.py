"""
cap08_lipschitz.py — codice del capitolo 8 (05-uniforme-continuita).
Eseguire dalla cartella Libro/:  python3 python/cap08_lipschitz.py
"""
import math, random

random.seed(1)
pend = []
for _ in range(100000):
    x, y = random.uniform(-10, 10), random.uniform(-10, 10)
    if x != y:
        pend.append(abs(math.sin(x) - math.sin(y)) / abs(x - y))
print(f"sen x: pendenza massima delle secanti = {max(pend):.6f}")
for h in (1e-2, 1e-4, 1e-6, 1e-8):
    print(f"sqrt(x): pendenza della secante tra 0 e {h:.0e}"
          f" = {math.sqrt(h) / h:7.0f}")

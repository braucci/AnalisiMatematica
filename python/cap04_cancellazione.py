"""
cap04_cancellazione.py — codice del capitolo 4 (04-proprieta).
Eseguire dalla cartella Libro/:  python3 python/cap04_cancellazione.py
"""
import math

# (1 - cos x)/x^2 -> 1/2. Due formule uguali in aritmetica esatta:
ingenua = lambda x: (1 - math.cos(x)) / x**2
# 1 - cos x = 2 sen^2(x/2): nessuna sottrazione tra numeri vicini
stabile = lambda x: 2 * math.sin(x / 2)**2 / x**2

for k in range(1, 10):
    x = 10.0**(-k)
    print(f"x = 1e-{k}:   ingenua = {ingenua(x):.10f}   "
          f"stabile = {stabile(x):.10f}")

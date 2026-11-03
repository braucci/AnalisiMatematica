"""
cap02_densita.py — codice del capitolo 2 (02-naturali-archimede).
Eseguire dalla cartella Libro/:  python3 python/cap02_densita.py
"""
# Il teorema di densità è costruttivo: la dimostrazione dice
# esattamente quali n e m scegliere. Traduciamola in codice, con
# l'aritmetica esatta delle frazioni.
from fractions import Fraction as F
import math

def razionale_tra(a, b):
    """Restituisce m/n con a < m/n < b, seguendo la dimostrazione."""
    assert a < b
    n = math.floor(1 / (b - a)) + 1     # Archimede: n > 1/(b - a)
    m = math.floor(n * a) + 1           # primo intero che supera n*a
    q = F(m, n)
    assert a < q < b                    # la tesi del teorema
    return q

print(razionale_tra(F(1, 3), F(1, 2)))         # tra 1/3 e 1/2
print(razionale_tra(math.sqrt(2), 1.4143))     # tra √2 e 1.4143
print(razionale_tra(math.pi, math.pi + 1e-6))  # intervallo minuscolo

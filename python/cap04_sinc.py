"""
cap04_sinc.py — codice del capitolo 4 (06-discontinuita).
Eseguire dalla cartella Libro/:  python3 python/cap04_sinc.py
"""
import math
import numpy as np

try:
    print(math.sin(0.0) / 0.0)
except ZeroDivisionError as err:
    print("sen(0)/0 ->", type(err).__name__, ":", err)

def sinc(x):
    """Prolungamento per continuità di sen(x)/x: vale 1 in x = 0."""
    return 1.0 if x == 0 else math.sin(x) / x

print(sinc(0.0), sinc(1e-9), sinc(math.pi / 2))
# NumPy usa la versione normalizzata sen(pi x)/(pi x), estesa in 0
print(np.sinc(0.0), np.sinc(0.5), np.sinc(1.0))

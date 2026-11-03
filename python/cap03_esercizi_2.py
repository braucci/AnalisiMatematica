"""
cap03_esercizi_2.py — codice del capitolo 3 (11-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap03_esercizi_2.py
"""
import math
a, x = 10.0, 1.0
r = math.sqrt(a)
for n in range(1, 9):
    print(f"x_{n} = {x:.15f}   errore = {abs(x - r):.1e}")
    x = (x + a / x) / 2

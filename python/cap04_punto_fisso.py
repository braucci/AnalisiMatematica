"""
cap04_punto_fisso.py — codice del capitolo 4 (11-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap04_punto_fisso.py
"""
import math

g = lambda x: math.cos(x) - x      # g(0) = 1 > 0, g(1) < 0
a, b = 0.0, 1.0
n = 0
while (b - a) / 2 >= 1e-12:        # errore del punto medio < 1e-12
    c = (a + b) / 2
    if g(c) > 0:                   # g decrescente: zero a destra
        a = c
    else:
        b = c
    n += 1
x = (a + b) / 2
print(f"x = {x:.12f}   cos x = {math.cos(x):.12f}   ({n} passi)")

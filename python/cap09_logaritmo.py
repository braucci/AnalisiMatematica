"""
cap09_logaritmo.py — codice del capitolo 9 (09-logaritmo).
Eseguire dalla cartella Libro/:  python3 python/cap09_logaritmo.py
"""
import math

def L(x, n=100000):
    """L(x) = int_1^x dt/t, formula del punto medio."""
    h = (x - 1) / n
    return h * sum(1 / (1 + (k + 0.5) * h) for k in range(n))

def E(y):
    """Inversa di L, per bisezione (L è crescente)."""
    a, b = 1e-6, 1e6
    for _ in range(80):
        m = math.sqrt(a * b)            # bisezione «geometrica»
        a, b = (m, b) if L(m, 2000) < y else (a, m)
    return math.sqrt(a * b)

for x in (0.5, 2, 3, 6, math.e):
    print(f"L({x:.4f}) = {L(x):.8f}   log = {math.log(x):.8f}")
print(f"L(2) + L(3) = {L(2) + L(3):.8f} = L(6)")
for y in (-1, 1, 2):
    print(f"E({y:2d}) = {E(y):.5f}   exp = {math.exp(y):.5f}")

"""
cap02_bombelli.py — codice del capitolo 2 (07-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap02_bombelli.py
"""
import cmath, math

def radici(z, n):
    rho, theta = cmath.polar(z)
    r = rho ** (1 / n)
    return [cmath.rect(r, (theta + 2 * k * math.pi) / n)
            for k in range(n)]

for w in radici(2 + 11j, 3):
    print(f"{w:.6f}")

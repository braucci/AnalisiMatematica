"""
cap11_riordinamenti.py — codice del capitolo 11 (08-assoluta).
Eseguire dalla cartella Libro/:  python3 python/cap11_riordinamenti.py
"""
import math

def riordina(L, N):
    """Somma N termini di 1 - 1/2 + 1/3 - ... riordinati in modo
    che le somme parziali tendano a L (algoritmo di Riemann)."""
    s, p, q = 0.0, 1, 2          # prossimo dispari, prossimo pari
    for _ in range(N):
        if s <= L:
            s += 1 / p; p += 2   # termine positivo
        else:
            s -= 1 / q; q += 2   # termine negativo
    return s

s, p, q = 0.0, 1, 2              # due positivi e un negativo
for _ in range(100000):
    s += 1 / p + 1 / (p + 2) - 1 / q
    p, q = p + 4, q + 2
print(f"due +, un -:  {s:.6f}   (3/2) log 2 = {1.5*math.log(2):.6f}")
for L in (0.0, 1.0, math.pi):
    print(f"obiettivo L = {L:.6f}:  "
          f"somma = {riordina(L, 10**6):.6f}")

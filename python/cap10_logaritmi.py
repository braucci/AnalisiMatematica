"""
cap10_logaritmi.py — codice del capitolo 10 (05-tabulazione).
Eseguire dalla cartella Libro/:  python3 python/cap10_logaritmi.py
"""
import math
from fractions import Fraction as F

def logN(N, tol=F(1, 10**13)):
    """log((N+1)/N) con x = 1/(2N+1), errore garantito < tol."""
    n = 0
    while F(1, 2*N*(N+1)*(2*n+3)*(2*N+1)**(2*n+1)) >= tol:
        n += 1
    x = F(1, 2*N + 1)
    T = 2 * sum(x**(2*k + 1) / (2*k + 1) for k in range(n + 1))
    return T, n + 1                  # valore e numero di termini

l2, t1 = logN(1)                     # log 2
l32, t2 = logN(2)                    # log 3/2
l54, t4 = logN(4)                    # log 5/4
l76, t6 = logN(6)                    # log 7/6
print("termini per N = 1, 2, 4, 6:", t1, t2, t4, t6)
tavola = {2: l2, 3: l2 + l32, 5: 2*l2 + l54}
tavola[7] = tavola[2] + tavola[3] + l76
for p, v in tavola.items():
    print(f"log {p} = {float(v):.12f}   (math.log: "
          f"{math.log(p):.12f})")
l10 = tavola[2] + tavola[5]
print(f"log10(2) = {float(tavola[2] / l10):.12f}")

"""
cap10_resto_cauchy.py — codice del capitolo 10 (04-resto-lagrange).
Eseguire dalla cartella Libro/:  python3 python/cap10_resto_cauchy.py
"""
import math

x = -0.8                          # log(1+x) con x < -1/2
q = abs(x) / (1 + x)              # = 4
print("  n    |R_n(x)|   Lagrange     Cauchy   integrale")
for n in (1, 2, 5, 10, 20, 40):
    T = sum((-1)**(k + 1) * x**k / k for k in range(1, n + 1))
    R = abs(math.log(1 + x) - T)
    lag = q**(n + 1) / (n + 1)
    cau = abs(x)**(n + 1) / (1 + x)
    itg = cau / (n + 1)
    print(f"{n:3d}  {R:.3e}  {lag:.3e}  {cau:.3e}  {itg:.3e}")

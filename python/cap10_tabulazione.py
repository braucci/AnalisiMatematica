"""
cap10_tabulazione.py — codice del capitolo 10 (05-tabulazione).
Eseguire dalla cartella Libro/:  python3 python/cap10_tabulazione.py
"""
import math
from fractions import Fraction as F

x = F(1, 10)
for n in (2, 4, 6):                  # sen x: T_n con n pari
    T = sum((-1)**k * x**(2*k+1) / math.factorial(2*k+1)
            for k in range(n // 2))
    stima = x**(n+1) / math.factorial(n+1)
    print(f"n={n}: T={float(T):.12f} stima={float(stima):.1e}")
print(f"math.sin(0.1) = {math.sin(0.1):.12f}")

n = 30                               # e con 31 termini, in frazioni
S = sum(F(1, math.factorial(k)) for k in range(n + 1))
stima = F(3, math.factorial(n + 1))
cifre = (S.numerator * 10**30) // S.denominator
print(f"e = 2.{str(cifre)[1:]}...  (errore < {float(stima):.1e})")
print(f"(1+1/n)^n, n=10^6: {(1 + 1e-6)**1e6:.10f}")

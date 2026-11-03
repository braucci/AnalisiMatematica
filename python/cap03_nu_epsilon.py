"""
cap03_nu_epsilon.py — codice del capitolo 3 (02-definizioni).
Eseguire dalla cartella Libro/:  python3 python/cap03_nu_epsilon.py
"""
# a_n = (2n+1)/(n+3) -> 2. Si ha |a_n - 2| = 5/(n+3), e la condizione
# |a_n - 2| < eps equivale a n > 5/eps - 3. Confrontiamo la formula
# con la ricerca "brutale" del primo indice da cui essa vale sempre.
from fractions import Fraction as F
import math

def a(n):
    return F(2 * n + 1, n + 3)

for eps in [F(1, 10), F(1, 100), F(1, 1000), F(1, 10**6)]:
    nu = max(0, math.floor(5 / eps - 3))   # disuguaglianza risolta
    primo = 1
    while abs(a(primo) - 2) >= eps:        # |a_n - 2| decresce
        primo += 1
    print(f"eps = {float(eps):.0e}:  nu = {nu:>7d},"
          f"  primo indice buono = {primo}")

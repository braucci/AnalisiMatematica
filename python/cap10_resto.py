"""
cap10_resto.py — codice del capitolo 10 (04-resto-lagrange).
Eseguire dalla cartella Libro/:  python3 python/cap10_resto.py
"""
import math
from scipy.integrate import quad

print(" n      R_n(1)       integrale       x_1     1/(n+2)")
for n in range(1, 8):
    T = sum(1 / math.factorial(k) for k in range(n + 1))
    R = math.e - T                                 # resto esatto
    I = quad(lambda t: (1 - t)**n / math.factorial(n)
             * math.exp(t), 0, 1)[0]               # resto integrale
    x1 = math.log(math.factorial(n + 1) * R)       # da e^x1/(n+1)!
    print(f"{n:2d}  {R:.9f}  {I:.9f}  {x1:.5f}  {1/(n+2):.5f}")

"""
cap11_serie_taylor.py — codice del capitolo 11 (09-serie-taylor).
Eseguire dalla cartella Libro/:  python3 python/cap11_serie_taylor.py
"""
import math

def exp_serie(x, N=100):
    """Somma dei primi N termini della serie esponenziale."""
    t, s = 1.0, 1.0
    for k in range(1, N):
        t *= x / k
        s += t
    return s

for x in (1.0, 5.0, -10.0, -20.0):
    print(f"x = {x:6.1f}: serie {exp_serie(x):.10e}   "
          f"exp {math.exp(x):.10e}")
print(f"e^-20 come 1/serie(20): {1 / exp_serie(20.0):.10e}")

lento = sum((-1)**(k - 1) / k for k in range(1, 11))
veloce = 2 * sum((1/3)**(2*k + 1) / (2*k + 1) for k in range(10))
print(f"log 2: lenta {lento:.6f}, veloce {veloce:.12f}, "
      f"esatto {math.log(2):.12f}")
print("e^(i pi) =", sum((1j * math.pi)**k / math.factorial(k)
                        for k in range(40)))

"""
cap08_esercizi.py — codice del capitolo 8 (07-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap08_esercizi.py
"""
import math

def punto_medio(f, a, b, n=100000):
    """Formula del punto medio con n intervalli."""
    h = (b - a) / n
    return h * sum(f(a + (k + 0.5) * h) for k in range(n))

i2 = punto_medio(lambda x: 2**x, 0, 1)
print(f"int_0^1 2^x dx = {i2:.8f}   1/log 2 = {1 / math.log(2):.8f}")
sc = punto_medio(lambda t: math.sqrt(1 - t * t), -1, 1)
print(f"int_-1^1 sqrt(1 - t^2) dt = {sc:.6f}"
      f"   pi/2 = {math.pi / 2:.6f}")
for n in (10, 100, 10000):
    a = sum(k * k for k in range(1, n + 1)) / n**3
    b = sum(n / (n * n + k * k) for k in range(1, n + 1))
    print(f"n = {n:5d}:  somma (a) = {a:.6f}   somma (b) = {b:.6f}")
print(f"1/3 = {1 / 3:.6f}   pi/4 = {math.pi / 4:.6f}")

"""
cap09_impropri.py — codice del capitolo 9 (08-impropri).
Eseguire dalla cartella Libro/:  python3 python/cap09_impropri.py
"""
import math

def punto_medio(f, a, b, n=200000):
    h = (b - a) / n
    return h * sum(f(a + (k + 0.5) * h) for k in range(n))

for B in (1, 2, 4, 6):
    I = punto_medio(lambda x: math.exp(-x * x), 0, B)
    print(f"int_0^{B} exp(-x^2) dx = {I:.10f}")
print(f"sqrt(pi)/2           = {math.sqrt(math.pi) / 2:.10f}")
for p in (0.5, 1, 2):
    v = [punto_medio(lambda x: x**-p, 1, B, 20000)
         for B in (10, 100, 1000)]
    print(f"p = {p}: int_1^B x^-p dx (B = 10, 100, 1000) =",
          ", ".join(f"{w:.3f}" for w in v))
g, R = 9.81, 6.371e6
print(f"velocità di fuga = {math.sqrt(2 * g * R) / 1000:.2f} km/s")

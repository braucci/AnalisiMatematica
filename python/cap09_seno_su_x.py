"""
cap09_seno_su_x.py — codice del capitolo 9 (08-impropri).
Eseguire dalla cartella Libro/:  python3 python/cap09_seno_su_x.py
"""
import math

def punto_medio(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (k + 0.5) * h) for k in range(n))

f = lambda x: math.sin(x) / x
g = lambda x: abs(math.sin(x)) / x
print("    B   int_0^B sen x/x   int_0^B |sen x|/x   (2/pi) log B")
for B in (10, 100, 1000, 10000):
    I = punto_medio(f, 0, B, 100 * B)
    J = punto_medio(g, 0, B, 100 * B)
    L = 2 / math.pi * math.log(B)
    print(f"{B:5d}   {I:15.6f}   {J:17.6f}   {L:12.6f}")
print(f"pi/2 = {math.pi / 2:.6f}")

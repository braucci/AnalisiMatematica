"""
cap04_sen_1_x.py — codice del capitolo 4 (03-legame-successioni).
Eseguire dalla cartella Libro/:  python3 python/cap04_sen_1_x.py
"""
import math

f = lambda x: math.sin(1 / x)

# x_n = 1/(n pi) e x'_n = 1/(pi/2 + 2 n pi) tendono entrambe a 0
print("      n      x_n        f(x_n)       x'_n        f(x'_n)")
for n in (1, 10, 100, 1000, 10**6):
    x = 1 / (n * math.pi)
    y = 1 / (math.pi / 2 + 2 * n * math.pi)
    print(f"{n:7d}   {x:.4e}  {f(x):+.2e}   {y:.4e}   {f(y):.12f}")

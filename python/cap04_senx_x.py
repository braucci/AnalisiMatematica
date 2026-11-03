"""
cap04_senx_x.py — codice del capitolo 4 (01-premessa).
Eseguire dalla cartella Libro/:  python3 python/cap04_senx_x.py
"""
import math

f = lambda x: math.sin(x) / x    # definita per x != 0, ed è pari

valori = [math.pi/2, math.pi/3, math.pi/4, math.pi/6,
          0.1, 0.01, 0.001, 1e-4, 1e-8]
for x in valori:
    print(f"x = {x:.8f}    f(x) = {f(x):.12f}")
print("f pari sui valori provati:",
      all(f(-x) == f(x) for x in valori))

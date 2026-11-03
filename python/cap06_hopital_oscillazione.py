"""
cap06_hopital_oscillazione.py — codice del capitolo 6 (05-hopital).
Eseguire dalla cartella Libro/:  python3 python/cap06_hopital_oscillazione.py
"""
import math

# f(x) = x + sen x, g(x) = x per x -> +oo: f/g -> 1, f'/g' oscilla
print("     x = k pi/2        f/g     f'/g' = 1 + cos x")
for k in (2000, 2001, 2002, 2003, 200000, 200001, 200002):
    x = k * math.pi / 2
    print(f"{x:15.4f}   {(x + math.sin(x)) / x:.6f}   "
          f"{1 + math.cos(x):.6f}")

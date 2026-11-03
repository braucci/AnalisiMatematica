"""
cap04_limiti_notevoli.py — codice del capitolo 4 (10-monotone-inverse).
Eseguire dalla cartella Libro/:  python3 python/cap04_limiti_notevoli.py
"""
import math

# log(1+x)/x -> 1 e (e^x - 1)/x -> 1 per x -> 0. Le funzioni
# log1p(x) = log(1+x), expm1(x) = e^x - 1 evitano la cancellazione.
print("    x     log(1+x)/x   log1p(x)/x   (e^x-1)/x    expm1(x)/x")
for k in (1, 3, 5, 8, 11, 14, 16):
    x = 10.0**(-k)
    a, b = math.log(1 + x) / x, math.log1p(x) / x
    c, d = (math.exp(x) - 1) / x, math.expm1(x) / x
    print(f"1e-{k:<3d} {a:12.10f} {b:12.10f} {c:12.10f} {d:12.10f}")

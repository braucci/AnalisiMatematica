"""
cap08_portanza_ellittica.py — codice del capitolo 8 (01-esaustione).
Eseguire dalla cartella Libro/:  python3 python/cap08_portanza_ellittica.py
"""
import math

b, W = 10.0, 10000.0                  # apertura [m], peso [N]
l0 = 4 * W / (math.pi * b)            # carico al centro [N/m]

def l(y):
    """Portanza per unità di apertura, distribuzione ellittica."""
    return l0 * math.sqrt(max(0.0, 1 - (2 * y / b)**2))

def strisce(n):
    """Somme per difetto e per eccesso con n strisce (n pari)."""
    y = [-b / 2 + k * b / n for k in range(n + 1)]
    s = S = 0.0
    for k in range(1, n + 1):
        lo, hi = sorted((l(y[k - 1]), l(y[k])))  # l monotona
        s += lo * (y[k] - y[k - 1])
        S += hi * (y[k] - y[k - 1])
    return s, S

print(f"l0 = {l0:.2f} N/m")
for n in (4, 16, 64, 256, 1024):
    s, S = strisce(n)
    print(f"n = {n:4d}: {s:8.1f} N <= L <= {S:8.1f} N"
          f"   (S - s = {S - s:6.1f} N)")

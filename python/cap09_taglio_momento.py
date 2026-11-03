"""
cap09_taglio_momento.py — codice del capitolo 9 (07-applicazioni).
Eseguire dalla cartella Libro/:  python3 python/cap09_taglio_momento.py
"""
import math

W, b = 10000.0, 10.0
s, l0 = b / 2, 4 * W / (math.pi * b)
l = lambda y: l0 * math.sqrt(max(0.0, 1 - (y / s)**2))

def T_esatto(y):
    u = y / s
    q = math.pi / 2 - math.asin(u) - u * math.sqrt(1 - u * u)
    return l0 * s / 2 * q

n = 5000                     # trapezi, dall'estremità alla radice
h = s / n
y = [s - k * h for k in range(n + 1)]
T, M = [0.0], [0.0]
for k in range(1, n + 1):
    T.append(T[-1] + h * (l(y[k - 1]) + l(y[k])) / 2)    # T' = -l
    M.append(M[-1] + h * (T[k - 1] + T[k]) / 2)          # M' = -T
print("  y [m]   T num. [N]  T esatto [N]   M num. [N m]")
for k in range(n, -1, -1000):
    print(f"{y[k]:6.1f}  {T[k]:10.1f}  {T_esatto(y[k]):11.1f}"
          f"  {M[k]:12.1f}")
print(f"M(0) esatto = W b/(3 pi) = {W * b / (3 * math.pi):.1f} N m")

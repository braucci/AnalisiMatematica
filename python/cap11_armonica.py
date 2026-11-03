"""
cap11_armonica.py — codice del capitolo 11 (05-armonica).
Eseguire dalla cartella Libro/:  python3 python/cap11_armonica.py
"""
import math

H, n = 0.0, 0
while H <= 10:                        # primo n con H_n > 10
    n += 1
    H += 1 / n
print(f"H_n > 10 per la prima volta con n = {n}")

H, N = 0.0, 1
for k in range(1, 10**6 + 1):
    H += 1 / k
    if k == N:
        print(f"n = {k:>7}:  H_n - log n = {H - math.log(k):.8f}")
        N *= 10

s = sum(1 / k**2 for k in range(1, 101))
print(f"pi^2/6 - s_100 = {math.pi**2 / 6 - s:.6f}"
      f"   (stima: tra {1/101:.6f} e {1/100:.6f})")

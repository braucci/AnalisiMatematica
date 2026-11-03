"""
cap11_alternate.py — codice del capitolo 11 (07-alternate).
Eseguire dalla cartella Libro/:  python3 python/cap11_alternate.py
"""
import math

s, err_max = 0.0, 0.0
for n in range(1, 10001):
    s += (-1)**(n - 1) / n
    errore = abs(s - math.log(2))
    err_max = max(err_max, errore * (n + 1))   # errore / a_(n+1)
    if n in (10, 99, 100, 1000, 10000):
        print(f"n = {n:5d}: s_n = {s:.8f}  errore = {errore:.2e}"
              f"  a_(n+1) = {1/(n+1):.2e}")
print(f"max di |s_n - log 2| / a_(n+1) = {err_max:.4f}  (<= 1)")

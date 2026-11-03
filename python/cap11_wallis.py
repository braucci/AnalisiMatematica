"""
cap11_wallis.py — codice del capitolo 11 (06-criteri).
Eseguire dalla cartella Libro/:  python3 python/cap11_wallis.py
"""
import math

W = 1.0                                   # prodotto parziale W_m
for m in range(1, 10**6 + 1):
    W *= 4 * m * m / (4 * m * m - 1)
    if m in (10, 100, 1000, 10**4, 10**5, 10**6):
        err = math.pi / 2 - W
        print(f"m = {m:>7}: W_m = {W:.9f}  errore = {err:.2e}"
              f"  m*errore = {m * err:.5f}")
print(f"pi/2 = {math.pi / 2:.9f},  pi/8 = {math.pi / 8:.5f}")

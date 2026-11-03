"""
cap03_gerarchia.py — codice del capitolo 3 (09-infiniti).
Eseguire dalla cartella Libro/:  python3 python/cap03_gerarchia.py
"""
import math

print(f"{'n':>4} {'log n':>8} {'n^2':>8} {'2^n':>12}"
      f" {'n!':>12} {'n^n':>12}")
for n in (5, 10, 20, 50, 100):
    print(f"{n:>4} {math.log(n):8.3f} {n**2:8d} {2.0**n:12.3e} "
          f"{float(math.factorial(n)):12.3e} {float(n)**n:12.3e}")

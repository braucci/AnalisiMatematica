"""
cap05_approssimazione.py — codice del capitolo 5 (06-tangente).
Eseguire dalla cartella Libro/:  python3 python/cap05_approssimazione.py
"""
import math

# tangente a sqrt in x0: sqrt(x) ~ sqrt(x0) + (x - x0) / (2 sqrt(x0))
lin = lambda x, x0: math.sqrt(x0) + (x - x0) / (2 * math.sqrt(x0))
casi = [(80, 81), (200, 196), (102, 100), (110, 100), (150, 100)]
for x, x0 in casi:
    e = lin(x, x0) - math.sqrt(x)
    print(f"sqrt({x}) ~ {lin(x, x0):.6f}  vero {math.sqrt(x):.6f}  "
          f"err {e:.1e}  rapporto {e / (x - x0)**2:.5f}")

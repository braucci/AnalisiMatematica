"""
cap10_orizzonte.py — codice del capitolo 10 (01-peano).
Eseguire dalla cartella Libro/:  python3 python/cap10_orizzonte.py
"""
import math

R = 6371.0                                 # raggio terrestre [km]
print(" h [km]   esatta [km]   sqrt(2Rh) [km]   differenza")
for h in (0.1, 1.0, 3.0, 10.0, 12.0):
    d = R * math.acos(R / (R + h))         # arco R*theta
    a = math.sqrt(2 * R * h)
    print(f"{h:6.1f}   {d:10.2f}    {a:12.2f}     {a - d:8.3f}")

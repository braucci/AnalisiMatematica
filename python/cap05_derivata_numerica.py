"""
cap05_derivata_numerica.py — codice del capitolo 5 (02-definizione).
Eseguire dalla cartella Libro/:  python3 python/cap05_derivata_numerica.py
"""
import math

x, esatta = 1.0, math.cos(1.0)        # f = sen, f'(1) = cos 1
print("   h       errore in avanti   errore centrato")
for k in range(1, 13, 1):
    h = 10.0**(-k)
    avanti = (math.sin(x + h) - math.sin(x)) / h
    centrata = (math.sin(x + h) - math.sin(x - h)) / (2 * h)
    ea, ec = abs(avanti - esatta), abs(centrata - esatta)
    print(f"1e-{k:<2d}   {ea:14.3e}   {ec:14.3e}")

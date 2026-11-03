"""
cap01_assiomi.py — codice del capitolo 1 (01-assiomi).
Eseguire dalla cartella Libro/:  python3 python/cap01_assiomi.py
"""
# Gli assiomi (A1)-(A6) si possono "toccare con mano" con numeri
# esatti: Fraction rappresenta i razionali senza arrotondamenti.
from fractions import Fraction as F

a, b, c = F(3, 4), F(-5, 6), F(7, 2)
print((a + b) + c == a + (b + c))      # (A1) associativa (somma)
print((a * b) * c == a * (b * c))      # (A1) associativa (prodotto)
print(a + b == b + a, a * b == b * a)  # (A2) commutativa
print(a * (b + c) == a * b + a * c)    # (A3) distributiva
print(a + 0 == a, a * 1 == a)          # (A4) elementi neutri
print(a + (-a) == 0)                   # (A5) opposto
print(a * (1 / a) == 1)                # (A6) inverso (a != 0)

"""
cap01_radice2.py — codice del capitolo 1 (04-nzq).
Eseguire dalla cartella Libro/:  python3 python/cap01_radice2.py
"""
# Costruiamo razionali in A (quadrato < 2) e in B (quadrato > 2)
# sempre più vicini tra loro; con Fraction restiamo sempre in Q.
from fractions import Fraction as F

a, b = F(1), F(2)              # a in A (1^2 < 2), b in B (2^2 > 2)
for passo in range(1, 31):
    m = (a + b) / 2            # punto medio: è ancora razionale
    if m * m < 2:
        a = m                  # m sta in A: alziamo a
    else:
        b = m                  # m sta in B: abbassiamo b
    if passo in (1, 2, 3, 10, 20, 30):
        print(f"passo {passo:2d}: {float(a):.12f} < √2 <",
              f"{float(b):.12f}   (b - a = {float(b - a):.2e})")
# La distanza b - a si dimezza a ogni passo e tende a zero, ma
# nessun razionale ha quadrato uguale a 2 (irrazionalità di √2):
print(any(x * x == 2 for x in (a, b)))

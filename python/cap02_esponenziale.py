"""
cap02_esponenziale.py — codice del capitolo 2 (03-radici-esponenziale).
Eseguire dalla cartella Libro/:  python3 python/cap02_esponenziale.py
"""
# Approssimiamo √2 per difetto con i troncamenti decimali y_k
# (numeri razionali) e calcoliamo 2**y_k: per la definizione di
# potenza reale come sup, i valori crescono e si avvicinano
# a 2**√2 senza superarlo.
from fractions import Fraction as F
import math

r2 = math.sqrt(2)
for k in range(1, 8):
    y = F(math.floor(r2 * 10**k), 10**k)   # troncamento < √2
    print(f"y = {str(y):>15s} = {float(y):.7f}"
          f"   2^y = {2 ** float(y):.10f}")
print(f"{'2^√2':>37s} = {2 ** r2:.10f}")

"""
cap03_erone.py — codice del capitolo 3 (07-monotone).
Eseguire dalla cartella Libro/:  python3 python/cap03_erone.py
"""
from decimal import Decimal, getcontext
getcontext().prec = 60              # lavoriamo con 60 cifre decimali

radice_vera = Decimal(2).sqrt()
x = Decimal(2)
for n in range(1, 8):
    errore = x - radice_vera
    print(f"x_{n} = {str(x)[:34]}   errore = {float(errore):.1e}")
    x = (x + 2 / x) / 2

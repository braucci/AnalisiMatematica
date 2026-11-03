"""
cap02_cifre_decimali.py — codice del capitolo 2 (02-naturali-archimede).
Eseguire dalla cartella Libro/:  python3 python/cap02_cifre_decimali.py
"""
# Le cifre di x dalla definizione c_k = [b^k x] - b [b^(k-1) x],
# in aritmetica intera esatta: m(k) deve restituire [b^k x].
import math
from fractions import Fraction as F

def cifre(m, n, b=10):
    """Restituisce la stringa 'c_0,c_1c_2...c_n' nella base b."""
    c = [m(k) - b * m(k - 1) for k in range(1, n + 1)]
    return f"{m(0)}," + "".join(str(ck) for ck in c)

# [10^k sqrt(2)] è il più grande intero j con j^2 <= 2 * 10^(2k)
print("sqrt(2) =", cifre(lambda k: math.isqrt(2 * 100**k), 40))
# 1/7: le cifre si ripetono con periodo 6
print("1/7     =", cifre(lambda k: math.floor(F(10**k, 7)), 36))
# 1/10 in base 2: periodico, quindi 0.1 non è esatto in un float
print("1/10    =", cifre(lambda k: math.floor(F(2**k, 10)), 36, b=2))
print("valore esatto di 0.1:", F(0.1))

"""
cap03_cauchy_razionali.py — codice del capitolo 3 (10-bw-cauchy).
Eseguire dalla cartella Libro/:  python3 python/cap03_cauchy_razionali.py
"""
# Troncamenti decimali di sqrt(2): sono razionali, distano sempre
# meno, ma il loro limite sqrt(2) non è razionale.
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 40
cifre = str(Decimal(2).sqrt())            # "1.414213562373095..."

tronc = [F(cifre[:2 + k]) for k in range(1, 12)]   # 1.4, 1.41, ...
print("k               q_k   max |q_j - q_k|, j > k   q_k^2 = 2 ?")
for k in range(1, 8):
    q = tronc[k - 1]
    dist = max(abs(tronc[j] - q) for j in range(k, len(tronc)))
    print(f"{k}  {str(q):>16s}   {float(dist):22.1e}   {q * q == 2}")

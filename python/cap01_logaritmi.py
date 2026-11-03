"""
cap01_logaritmi.py — codice del capitolo 1 (08-potenze-esp-log).
Eseguire dalla cartella Libro/:  python3 python/cap01_logaritmi.py
"""
import math
# La definizione: log_a(x) è l'esponente y tale che a**y == x
a, x = 2.0, 10.0
y = math.log(x, a)                     # logaritmo in base a
print(f"log_2(10) = {y:.6f},   2**{y:.6f} = {a**y:.6f}")

# Proprietà (log1), (log3), (log4) verificate numericamente
x1, x2, b = 3.0, 7.0, 2.5
print(math.isclose(math.log(x1*x2), math.log(x1) + math.log(x2)))
print(math.isclose(math.log(x1**b), b*math.log(x1)))
print(math.isclose(math.log(x1, 10), math.log(x1)/math.log(10)))

# Il numero di Nepero come limite di (1 + 1/n)**n
for n in (1, 10, 100, 1000, 10**6):
    print(f"n = {n:>8d}   (1+1/n)^n = {(1 + 1/n)**n:.8f}")
print(f"math.e         = {math.e:.8f}")

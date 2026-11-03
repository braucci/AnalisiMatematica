"""
cap01_induzione.py — codice del capitolo 1 (10-induzione).
Eseguire dalla cartella Libro/:  python3 python/cap01_induzione.py
"""
import sympy as sp
n, k, x = sp.symbols("n k x", positive=True, integer=True)

# sympy calcola le somme in forma chiusa: confrontiamo con le nostre
print(sp.factor(sp.summation(k, (k, 1, n))))          # Gauss
print(sp.factor(sp.summation(k**2, (k, 1, n))))       # quadrati
s = sp.summation(1/(k*(k+1)), (k, 1, n))
print(sp.simplify(s))                                 # telescopica

# Il passo induttivo della somma dei quadrati: due polinomi uguali?
print(sp.expand(2*n**2 + 7*n + 6 - (n + 2)*(2*n + 3)) == 0)

# Forza bruta: controlliamo la formula di Gauss per n = 1, ..., 1000
ok = (sum(range(1, m + 1)) == m*(m + 1)//2 for m in range(1, 1001))
print(all(ok))

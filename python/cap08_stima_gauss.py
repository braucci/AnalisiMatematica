"""
cap08_stima_gauss.py — codice del capitolo 8 (03-proprieta).
Eseguire dalla cartella Libro/:  python3 python/cap08_stima_gauss.py
"""
import math

f = lambda x: math.exp(-x * x)        # decrescente in [0, 1]

def somme_decrescente(f, a, b, n):
    """s(P) e S(P) per la partizione uniforme, f decrescente."""
    h = (b - a) / n
    x = [a + k * h for k in range(n + 1)]
    s = h * sum(f(x[k]) for k in range(1, n + 1))      # m_k
    S = h * sum(f(x[k - 1]) for k in range(1, n + 1))  # M_k
    return s, S

for n in (10, 100, 1000, 10000):
    s, S = somme_decrescente(f, 0.0, 1.0, n)
    print(f"n = {n:5d}:  {s:.6f} <= I <= {S:.6f}"
          f"   S - s = {S - s:.2e}")
print(f"(1 - 1/e)/10000 = {(1 - math.exp(-1)) / 10000:.2e}")
ref = math.erf(1) * math.sqrt(math.pi) / 2
print(f"valore di riferimento (funzione erf): {ref:.6f}")

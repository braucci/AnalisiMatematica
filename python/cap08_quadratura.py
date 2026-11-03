"""
cap08_quadratura.py — codice del capitolo 8 (06-integrabilita).
Eseguire dalla cartella Libro/:  python3 python/cap08_quadratura.py
"""
import math

f = lambda x: math.exp(-x * x)
I = math.erf(1) * math.sqrt(math.pi) / 2     # valore di riferimento

def quadrature(f, a, b, n):
    """Rettangoli, punto medio, trapezi, Cavalieri-Simpson."""
    h = (b - a) / n
    x = [a + k * h for k in range(n + 1)]
    ret = h * sum(f(x[k]) for k in range(n))
    med = h * sum(f(x[k] + h / 2) for k in range(n))
    tra = h * (sum(f(t) for t in x) - (f(a) + f(b)) / 2)
    return ret, med, tra, (2 * med + tra) / 3

print("errori assoluti")
print(f"{'n':>4} {'rettangoli':>11} {'p. medio':>10}"
      f" {'trapezi':>10} {'Simpson':>10}")
for n in (4, 8, 16, 32, 64):
    err = [abs(q - I) for q in quadrature(f, 0, 1, n)]
    print(f"{n:4d} " + " ".join(f"{e:10.2e}" for e in err))

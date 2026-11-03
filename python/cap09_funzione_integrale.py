"""
cap09_funzione_integrale.py — codice del capitolo 9 (01-teorema-fondamentale).
Eseguire dalla cartella Libro/:  python3 python/cap09_funzione_integrale.py
"""
import math

f = lambda t: math.exp(-t * t)

def F(x, n=2000):
    """Funzione integrale int_0^x f(t) dt (punto medio)."""
    h = x / n
    return h * sum(f((k + 0.5) * h) for k in range(n))

h = 1e-3
print("  x      F(x)  sqrt(pi)/2 erf(x)   rapp. incr.     f(x)")
for x in (0.0, 0.5, 1.0, 1.5, 2.0):
    rif = math.sqrt(math.pi) / 2 * math.erf(x)
    d = (F(x + h) - F(x - h)) / (2 * h)
    print(f"{x:4.1f}  {F(x):.6f}      {rif:.6f}      {d:.6f}"
          f"   {f(x):.6f}")

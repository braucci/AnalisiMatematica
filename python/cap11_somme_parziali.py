"""
cap11_somme_parziali.py — codice del capitolo 11 (01-serie-numeriche).
Eseguire dalla cartella Libro/:  python3 python/cap11_somme_parziali.py
"""
import math

def somme_parziali(a, N):
    """Restituisce la lista s_1, ..., s_N delle somme parziali."""
    s, out = 0.0, []
    for k in range(1, N + 1):
        s += a(k)
        out.append(s)
    return out

serie = {
    "Mengoli": lambda k: 1 / (k * (k + 1)),
    "radici":  lambda k: 1 / (math.sqrt(k + 1) + math.sqrt(k)),
    "(-1)^k":  lambda k: (-1)**k,
}
for nome, a in serie.items():
    s = somme_parziali(a, 10000)
    print(f"{nome:8s}: s_10 = {s[9]:9.5f}  s_100 = {s[99]:9.5f}"
          f"  s_10000 = {s[-1]:9.5f}")

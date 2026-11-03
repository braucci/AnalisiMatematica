"""
cap08_darboux.py — codice del capitolo 8 (02-definizione).
Eseguire dalla cartella Libro/:  python3 python/cap08_darboux.py
"""
def darboux(f, a, b, n, critici=()):
    """Somme s(P), S(P) per la partizione uniforme in n parti:
    m_k e M_k si cercano tra gli estremi dell'intervallo e i
    punti critici interni (Weierstrass + Fermat)."""
    x = [a + k * (b - a) / n for k in range(n + 1)]
    s = S = 0.0
    for k in range(1, n + 1):
        cand = [x[k - 1], x[k]]
        cand += [c for c in critici if x[k - 1] < c < x[k]]
        v = [f(t) for t in cand]
        s += min(v) * (x[k] - x[k - 1])
        S += max(v) * (x[k] - x[k - 1])
    return s, S

f = lambda x: x**3 - 3 * x            # punti critici: -1 e 1
for n in (3, 30, 300, 3000):
    s, S = darboux(f, -2, 2, n, critici=(-1, 1))
    print(f"n = {n:4d}: s = {s:9.5f}  S = {S:8.5f}"
          f"  S-s = {S - s:8.5f}  n(S-s) = {n * (S - s):5.2f}")

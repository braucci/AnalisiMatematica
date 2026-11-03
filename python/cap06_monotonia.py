"""
cap06_monotonia.py — codice del capitolo 6 (03-monotonia).
Eseguire dalla cartella Libro/:  python3 python/cap06_monotonia.py
"""
import sympy as sp

x = sp.symbols("x", real=True)

def punto_interno(p, q):
    """Un punto di prova nell'intervallo aperto (p, q)."""
    if p.is_finite and q.is_finite:
        return (p + q) / 2
    if p.is_finite:
        return p + 1
    return q - 1 if q.is_finite else sp.Integer(0)

def tabella_monotonia(f):
    """Intervalli di monotonia di f su R, dal segno di f'."""
    df = sp.factor(sp.diff(f, x))
    critici = sorted(sp.solveset(df, x, sp.S.Reals))
    print(f"f = {f},   f' = {df},   f' = 0 in {critici}")
    nodi = [-sp.oo] + critici + [sp.oo]
    for p, q in zip(nodi[:-1], nodi[1:]):
        s = sp.sign(df.subs(x, punto_interno(p, q)))
        verso = "crescente" if s > 0 else "decrescente"
        print(f"  ({p}, {q}):  f' {'+' if s > 0 else '-'}  {verso}")

tabella_monotonia(x**3 - 3*x)
tabella_monotonia(x**4 - 2*x**2)

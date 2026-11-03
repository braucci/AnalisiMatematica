"""
cap06_estremi.py — codice del capitolo 6 (01-fermat).
Eseguire dalla cartella Libro/:  python3 python/cap06_estremi.py
"""
import sympy as sp

x = sp.symbols("x", real=True)

def estremi_assoluti(f, a, b):
    """Massimo e minimo assoluti di f (derivabile) in [a, b]."""
    critici = sp.solveset(sp.diff(f, x), x, sp.Interval.open(a, b))
    candidati = sorted(set(critici) | {a, b})
    valori = {c: f.subs(x, c) for c in candidati}
    for c in candidati:
        print(f"  f({c}) = {valori[c]}")
    M, m = max(valori.values()), min(valori.values())
    dove = lambda y: [c for c in candidati if valori[c] == y]
    print("  max =", M, "in", dove(M))
    print("  min =", m, "in", dove(m))

print("f(x) = x^3 - 3x in [-2, 3]:")
estremi_assoluti(x**3 - 3*x, -2, 3)

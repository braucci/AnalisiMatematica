"""
cap06_trave.py — codice del capitolo 6 (09-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap06_trave.py
"""
import sympy as sp

b, d = sp.symbols("b d", positive=True)
h2 = d**2 - b**2                  # Pitagora: b^2 + h^2 = d^2
Wf = b * h2 / 6                   # modulo di resistenza b h^2 / 6
bs = sp.solve(sp.diff(Wf, b), b)[0]
print("b* =", bs, "  h* =", sp.sqrt(h2.subs(b, bs)),
      "  h*/b* =", sp.simplify(sp.sqrt(h2.subs(b, bs)) / bs))
print("W'' (b*) =", sp.simplify(sp.diff(Wf, b, 2).subs(b, bs)))
print("W_max =", sp.simplify(Wf.subs(b, bs)))

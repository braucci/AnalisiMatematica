"""
cap02_tartaglia.py — codice del capitolo 2 (05-binomio).
Eseguire dalla cartella Libro/:  python3 python/cap02_tartaglia.py
"""
import sympy as sp

def tartaglia(righe):
    riga = [1]
    for n in range(righe):
        yield riga
        # formula di Stifel: ogni elemento interno è la somma
        # dei due elementi che gli stanno sopra
        riga = ([1] + [riga[k - 1] + riga[k]
                       for k in range(1, len(riga))] + [1])

for riga in tartaglia(8):
    print(" ".join(f"{c:3d}" for c in riga).center(40))

a, b = sp.symbols("a b")
print(sp.expand((a + b)**5))

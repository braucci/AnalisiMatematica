"""
cap03_forme_indeterminate.py — codice del capitolo 3 (04-forme-indeterminate).
Eseguire dalla cartella Libro/:  python3 python/cap03_forme_indeterminate.py
"""
# Prodotti "zero per infinito": un fattore tende a 0, l'altro
# diverge; il comportamento dipende dalle velocità relative.
casi = {
    "(1/n) * n^2":      lambda n: (1 / n) * n**2,
    "(1/n) * 3n":       lambda n: (1 / n) * 3 * n,
    "(1/n^2) * n":      lambda n: (1 / n**2) * n,
    "((-1)^n/n) * n":   lambda n: ((-1)**n / n) * n,
}
indici = (10, 11, 1000, 1001)
for nome, a in casi.items():
    valori = "  ".join(f"{a(n):>10.4g}" for n in indici)
    print(f"{nome:>16s}:  {valori}")

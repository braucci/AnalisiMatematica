"""
cap01_insiemi.py — codice del capitolo 1 (03-insiemi).
Eseguire dalla cartella Libro/:  python3 python/cap01_insiemi.py
"""
# Python ha un tipo nativo per gli insiemi finiti: set.
S = set(range(1, 13))               # S = {1, 2, ..., 12}
A = {n for n in S if n % 2 == 0}    # i pari, "per proprietà"
B = {n for n in S if n <= 7}
print("A ∩ B =", A & B)             # intersezione
print("A ∪ B =", A | B)             # unione
print("A \\ B =", A - B)            # differenza
print("B ⊆ A ?", B <= A)            # inclusione
print("A^c   =", S - A)             # complementare rispetto a S

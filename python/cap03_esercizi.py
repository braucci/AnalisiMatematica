"""
cap03_esercizi.py — codice del capitolo 3 (11-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap03_esercizi.py
"""
a = lambda n: n**10 / 1.1**n
n_max = max(range(1, 1000), key=a)
print("massimo per n =", n_max, f"  a(n) = {a(n_max):.3e}")
print(f"a(500) = {a(500):.3e},  a(1000) = {a(1000):.3e}")

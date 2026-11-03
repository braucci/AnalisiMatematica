"""
cap01_bisezione.py — codice del capitolo 1 (11-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap01_bisezione.py
"""
def radice(y, n):
    a, b = 0.0, max(1.0, y)          # a^2 <= y <= b^2
    iterazioni = 0
    while b - a >= 10**(-n):
        m = (a + b) / 2
        if m * m < y:
            a = m                    # m è "troppo piccolo"
        else:
            b = m                    # m è "troppo grande"
        iterazioni += 1
    return (a + b) / 2, iterazioni

print(radice(2, 12))                 # (1.414213562372879, 41)

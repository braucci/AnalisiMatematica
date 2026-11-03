"""
cap11_geometrica.py — codice del capitolo 11 (04-geometrica).
Eseguire dalla cartella Libro/:  python3 python/cap11_geometrica.py
"""
from fractions import Fraction as F

def periodico(antiperiodo, periodo):
    """Frazione di 0,antiperiodo(periodo), es. ('1', '6') -> 1/6."""
    m, p = len(antiperiodo), len(periodo)
    A = int(antiperiodo) if antiperiodo else 0
    C = int(periodo)
    # 0,a(c) = (A + C/(10^p - 1)) / 10^m
    return (A + F(C, 10**p - 1)) / 10**m

for a, c in (("", "13"), ("", "9"), ("1", "6"), ("", "142857")):
    print(f"0,{a}({c}) = {periodico(a, c)}")

x = 0.6                                    # somme parziali, q = 0,6
s = [sum(x**k for k in range(n + 1)) for n in (5, 10, 20, 40)]
print("s_n:", [round(v, 8) for v in s], " 1/(1-x) =", 1 / (1 - x))

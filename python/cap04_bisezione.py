"""
cap04_bisezione.py — codice del capitolo 4 (08-bisezione).
Eseguire dalla cartella Libro/:  python3 python/cap04_bisezione.py
"""
import math

def bisezione(f, a, b, passi):
    """Se f(a) < 0 < f(b), restituisce i punti medi c_0, ..., c_n."""
    assert f(a) < 0 < f(b)
    medi = []
    for n in range(passi + 1):
        c = (a + b) / 2
        medi.append(c)
        if f(c) == 0:          # radice esatta: ci si ferma
            break
        if f(c) > 0:
            b = c              # il cambio di segno è in [a, c]
        else:
            a = c              # il cambio di segno è in [c, b]
    return medi

f1 = lambda x: x**3 + x - 1           # f1(0) = -1 < 0 < 1 = f1(1)
f2 = lambda x: math.exp(x) + x        # f2(-1) = 1/e - 1 < 0 < f2(0)

c1 = bisezione(f1, 0, 1, 9)
c2 = bisezione(f2, -1, 0, 9)
for n in range(10):
    print(f"c_{n} = {c1[n]:.6f}     c_{n} = {c2[n]:+.6f}")

# 50 passi: errore < 2^-51; confronto con la formula di Cardano
r1 = bisezione(f1, 0, 1, 50)[-1]
s = math.sqrt(31 / 108)
cardano = (0.5 + s) ** (1/3) - (s - 0.5) ** (1/3)
print(f"x^3 + x - 1 = 0:  {r1:.15f}   (Cardano: {cardano:.15f})")
print(f"e^x + x = 0:     {bisezione(f2, -1, 0, 50)[-1]:.15f}")

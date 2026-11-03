"""
cap02_sup_bisezione.py — codice del capitolo 2 (01-sup-inf).
Eseguire dalla cartella Libro/:  python3 python/cap02_sup_bisezione.py
"""
# Se A è chiuso verso sinistra (x in A e y < x implicano y in A),
# come A = {x : x^3 < 5}, l'estremo superiore si approssima per
# bisezione: si tengono un punto a in A e un maggiorante b, e si
# dimezza ogni volta l'intervallo [a, b].
def sup_bisezione(appartiene, a, b, tol=1e-12):
    """a deve stare in A, b deve essere un maggiorante di A."""
    while b - a > tol:
        m = (a + b) / 2
        if appartiene(m):
            a = m          # m sta in A: il sup è almeno m
        else:
            b = m          # m non sta in A: è un maggiorante
    return a, b

# A = {x : x^3 < 5}: 0 sta in A, 5 è un maggiorante, e sup A è
# la radice cubica di 5
a, b = sup_bisezione(lambda x: x**3 < 5, 0.0, 5.0)
print(f"{a:.14f} <= sup A <= {b:.14f}")
print(f"5 ** (1/3) = {5 ** (1/3):.14f}")

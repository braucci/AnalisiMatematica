"""
cap04_kepler.py — codice del capitolo 4 (11-esercizi).
Eseguire dalla cartella Libro/:  python3 python/cap04_kepler.py
"""
import math

def bisezione(f, a, b, tol):
    """Approssima uno zero di f in [a, b] con errore < tol."""
    assert f(a) <= 0 <= f(b)
    passi = 0
    while (b - a) / 2 >= tol:      # errore del punto medio
        c = (a + b) / 2
        if f(c) > 0:
            b = c
        else:
            a = c
        passi += 1
    return (a + b) / 2, passi

e, M = 0.5, 1.0                    # eccentricità, anomalia media
kepler = lambda E: E - e * math.sin(E) - M
E, passi = bisezione(kepler, 0, math.pi, 1e-10)
print(f"E = {E:.10f} rad  dopo {passi} dimezzamenti")
print(f"verifica: E - e sen E = {E - e * math.sin(E):.10f}")

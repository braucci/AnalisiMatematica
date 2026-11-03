"""
cap07_minimi_quadrati.py — codice del capitolo 7 (05-massimi-minimi).
Eseguire dalla cartella Libro/:  python3 python/cap07_minimi_quadrati.py
"""
import numpy as np

# "prove in galleria": C_D misurato per vari C_L (dati simulati)
rng = np.random.default_rng(7)
CL = np.linspace(0.0, 1.2, 13)
CD = 0.025 + 0.0497 * CL**2 + rng.normal(0, 0.0008, CL.size)

# modello C_D = b + a X con X = C_L^2: equazioni normali
X, n = CL**2, CL.size
A = np.array([[np.sum(X**2), np.sum(X)], [np.sum(X), n]])
r = np.array([np.sum(X * CD), np.sum(CD)])
a, b = np.linalg.solve(A, r)
H = 4 * (n * np.sum(X**2) - np.sum(X)**2)   # hessiano di S(a, b)
print(f"k = a = {a:.5f}   C_D0 = b = {b:.5f}   H = {H:.2f} > 0")
print(f"fattore di Oswald (AR = 8): e = {1 / (np.pi * 8 * a):.3f}")
print("controllo con numpy.polyfit:",
      np.round(np.polyfit(X, CD, 1), 5))
S = np.sum((CD - b - a * X)**2)
print(f"somma dei quadrati dei residui S = {S:.3e}")

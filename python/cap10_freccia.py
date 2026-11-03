"""
cap10_freccia.py — codice del capitolo 10 (03-resto-integrale).
Eseguire dalla cartella Libro/:  python3 python/cap10_freccia.py
"""
import math
from scipy.integrate import quad

W, b, EI = 10000.0, 10.0, 2.0e6            # N, m, N*m^2
s = b / 2
carichi = {
    "uniforme": lambda y: W / b,
    "ellittico": lambda y: 4 * W / (math.pi * b)
                           * math.sqrt(max(0.0, 1 - (y / s)**2)),
}
v_tip = {}
for nome, l in carichi.items():
    M = lambda t: quad(lambda e: (e - t) * l(e), t, s)[0]
    v_tip[nome] = quad(lambda t: (s - t) * M(t), 0, s)[0] / EI
    print(f"{nome:9s}:  v(s) = {100 * v_tip[nome]:.3f} cm")
print(f"formula l*s^4/(8EI): {100 * (W/b) * s**4 / (8*EI):.3f} cm")
print(f"rapporto ellittico/uniforme = "
      f"{v_tip['ellittico'] / v_tip['uniforme']:.4f}")

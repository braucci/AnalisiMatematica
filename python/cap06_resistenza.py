"""
cap06_resistenza.py — codice del capitolo 6 (06-studio).
Eseguire dalla cartella Libro/:  python3 python/cap06_resistenza.py
"""
import math

# velivolo leggero, volo livellato al livello del mare
W, S, rho = 10000.0, 16.0, 1.225        # peso (N), superficie (m^2)
CD0, AR, e = 0.025, 8.0, 0.8
k = 1 / (math.pi * e * AR)
a = 0.5 * rho * S * CD0                 # D(V) = a V^2 + b / V^2
b = 2 * k * W**2 / (rho * S)
D = lambda V: a * V**2 + b / V**2
P = lambda V: D(V) * V                  # potenza necessaria

V_D = (b / a) ** 0.25                   # minimo di D: D'(V) = 0
V_P = (b / (3 * a)) ** 0.25             # minimo di P: P'(V) = 0
print(f"k = {k:.5f}   a = {a:.4f}   b = {b:.4e}")
print(f"V_minD = {V_D:.2f} m/s   D_min = {D(V_D):.1f} N"
      f"   W/D_min = {W / D(V_D):.2f}")
print(f"V_minP = {V_P:.2f} m/s   P_min = {P(V_P) / 1000:.2f} kW")
print(f"V_minD / V_minP = {V_D / V_P:.4f}   3^(1/4) = {3**0.25:.4f}")
CLmax = 1.5                             # C_L massimo (stallo)
print(f"V_stallo = {math.sqrt(2 * W / (rho * S * CLmax)):.2f} m/s")

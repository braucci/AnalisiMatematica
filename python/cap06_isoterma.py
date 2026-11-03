"""
cap06_isoterma.py — codice del capitolo 6 (03-monotonia).
Eseguire dalla cartella Libro/:  python3 python/cap06_isoterma.py
"""
import math

# ISA, strato isotermo tra 11 e 20 km
R, g, T = 287.05, 9.80665, 216.65        # J/(kg K), m/s^2, K
z1, p1 = 11000.0, 22632.0                # m, Pa (tropopausa)
H = R * T / g                            # altezza di scala
p = lambda z: p1 * math.exp(-(z - z1) / H)
print(f"H = {H:.1f} m")
for z in (11000, 14000, 17000, 20000):
    rho = p(z) / (R * T)
    print(f"z = {z:5d} m   p = {p(z):8.1f} Pa"
          f"   rho = {rho:.4f} kg/m^3")

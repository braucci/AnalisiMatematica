"""
cap05_isa.py — codice del capitolo 5 (05-elementari).
Eseguire dalla cartella Libro/:  python3 python/cap05_isa.py
"""
# Densità ISA (troposfera): rho0 (1 - L h/T0)^n, n = g/(R L) - 1
rho0, T0, L, g, R = 1.225, 288.15, 0.0065, 9.80665, 287.05
n = g / (R * L) - 1
rho = lambda h: rho0 * (1 - L * h / T0) ** n
# derivata con la regola della catena: D[u^n] = n u^(n-1) u'
drho = lambda h: rho0 * n * (1 - L * h / T0) ** (n - 1) * (-L / T0)

vz = 5.0                               # velocità verticale (m/s)
print(f"n = {n:.4f}")
print("    h      rho      drho/dh     numerica     drho/dt")
for h in (0, 2000, 5000, 10000):
    num = (rho(h + 0.01) - rho(h - 0.01)) / 0.02  # diff. centrata
    print(f"{h:5d}   {rho(h):.4f}  {drho(h):.4e}  {num:.4e}  "
          f"{drho(h) * vz:.3e}")

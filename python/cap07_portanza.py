"""
cap07_portanza.py — codice del capitolo 7 (01-due-variabili).
Eseguire dalla cartella Libro/:  python3 python/cap07_portanza.py
"""
rho, S, W = 1.225, 16.0, 10000.0         # kg/m^3, m^2, N
L = lambda V, CL: 0.5 * rho * S * V**2 * CL

CLs = (0.2, 0.4, 0.6, 0.8, 1.0, 1.2)
print(" V (m/s) |" + "".join(f"   CL={c:.1f}" for c in CLs))
for V in (30, 40, 50, 60, 70):
    riga = "".join(f"{L(V, c):9.0f}" for c in CLs)
    print(f"  {V:5d}  |{riga}")
# le coppie (V, C_L) per cui L = W: C_L = 2W / (rho S V^2)
for V in (30, 40, 50, 60, 70):
    print(f"V = {V} m/s:  L = W per C_L = "
          f"{2 * W / (rho * S * V**2):.3f}")

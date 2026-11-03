"""
cap07_sensibilita.py — codice del capitolo 7 (03-derivate-parziali).
Eseguire dalla cartella Libro/:  python3 python/cap07_sensibilita.py
"""
import math

# C_D(C_L, AR) = C_D0 + C_L^2 / (pi e AR): sensibilità parziali
CD0, e = 0.025, 0.8
CD = lambda CL, AR: CD0 + CL**2 / (math.pi * e * AR)
dCD_dCL = lambda CL, AR: 2 * CL / (math.pi * e * AR)
dCD_dAR = lambda CL, AR: -CL**2 / (math.pi * e * AR**2)
print("  C_L  AR     C_D     dC_D/dC_L   dC_D/dAR")
for CL, AR in ((0.5, 8), (1.0, 8), (1.0, 12)):
    print(f"  {CL:.1f}  {AR:2d}   {CD(CL, AR):.5f}   "
          f"{dCD_dCL(CL, AR):.5f}    {dCD_dAR(CL, AR):.6f}")

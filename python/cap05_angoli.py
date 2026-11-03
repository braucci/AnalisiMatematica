"""
cap05_angoli.py — codice del capitolo 5 (07-trig-inverse).
Eseguire dalla cartella Libro/:  python3 python/cap05_angoli.py
"""
import math

# velocità in assi corpo (m/s): u avanti, v laterale, w in basso
casi = [(60.0, 0.0, 5.0), (60.0, 3.0, -4.0), (-2.0, 0.0, 10.0)]
for u, v, w in casi:
    V = math.sqrt(u*u + v*v + w*w)
    alfa_atan = math.degrees(math.atan(w / u))  # in (-90°, 90°)
    alfa = math.degrees(math.atan2(w, u))       # vede il quadrante
    beta = math.degrees(math.asin(v / V))       # derapata
    print(f"u={u:5.1f} v={v:3.1f} w={w:5.1f}: "
          f"atan {alfa_atan:7.2f}°  atan2 {alfa:7.2f}°"
          f"  beta {beta:5.2f}°")

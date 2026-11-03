"""
cap03_archimede.py — codice del capitolo 3 (01-premessa).
Eseguire dalla cartella Libro/:  python3 python/cap03_archimede.py
"""
# s = semiperimetro del poligono inscritto, t = del circoscritto
# (raggio 1). Da n a 2n lati (media armonica e media geometrica):
#     t_2n = 2 s t / (s + t),      s_2n = sqrt(s * t_2n)
# Si parte dall'esagono: s_6 = 3, t_6 = 2*sqrt(3). Niente pi greco!
import math

n, s, t = 6, 3.0, 2 * math.sqrt(3)
print(f"{n:4d} lati: {s:.6f} < pi < {t:.6f}")
for _ in range(4):               # quattro raddoppi, fino a 96 lati
    t = 2 * s * t / (s + t)
    s = math.sqrt(s * t)
    n *= 2
    print(f"{n:4d} lati: {s:.6f} < pi < {t:.6f}")
print(f"Archimede: {223/71:.6f} < pi < {22/7:.6f}")

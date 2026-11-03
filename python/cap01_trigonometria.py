"""
cap01_trigonometria.py — codice del capitolo 1 (09-trigonometriche).
Eseguire dalla cartella Libro/:  python3 python/cap01_trigonometria.py
"""
import math
# Relazione fondamentale e duplicazione, per angoli "a caso"
for x in (0.3, 1.0, 2.5, -4.0):
    print(math.isclose(math.sin(x)**2 + math.cos(x)**2, 1.0),
          math.isclose(math.sin(2*x), 2*math.sin(x)*math.cos(x)))

# Le disuguaglianze 0 < sen x < x < tg x per 0 < x < pi/2
for x in (0.1, 0.5, 1.0, 1.5):
    s, t = math.sin(x), math.tan(x)
    print(f"x={x:.1f}:  sen x={s:.4f} < x={x:.4f} < tg x={t:.4f}")

# I valori notevoli: math.radians converte i gradi in radianti
for gradi in (0, 30, 45, 60, 90):
    x = math.radians(gradi)
    print(f"{gradi:3d}°  sen={math.sin(x):.4f}"
          f"  cos={math.cos(x):.4f}")

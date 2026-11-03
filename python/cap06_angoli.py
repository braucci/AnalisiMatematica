"""
cap06_angoli.py — codice del capitolo 6 (07-taylor).
Eseguire dalla cartella Libro/:  python3 python/cap06_angoli.py
"""
import math

print(" phi(gradi)  sen phi    phi    errore   1/cos phi  1+phi^2/2")
for g in (5, 10, 15, 20, 30, 45, 60):
    phi = math.radians(g)
    s = math.sin(phi)
    print(f"{g:8d}    {s:.5f}  {phi:.5f}  {(phi - s) / s:7.2%}"
          f"    {1 / math.cos(phi):.4f}    {1 + phi**2 / 2:.4f}")

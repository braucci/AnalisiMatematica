"""
cap03_piccoli_angoli.py — codice del capitolo 3 (06-limiti-notevoli).
Eseguire dalla cartella Libro/:  python3 python/cap03_piccoli_angoli.py
"""
import math

print(" gradi   radianti   sen(a)/a   errore %   stima a^2/2 %")
for gradi in (1, 2, 5, 10, 15, 20, 30):
    a = math.radians(gradi)
    r = math.sin(a) / a
    print(f"{gradi:5d}   {a:8.5f}   {r:8.6f}   {100*(1-r):7.4f}"
          f"    {100*a*a/2:8.4f}")

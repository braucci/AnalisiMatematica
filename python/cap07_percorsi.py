"""
cap07_percorsi.py — codice del capitolo 7 (02-limiti-continuita).
Eseguire dalla cartella Libro/:  python3 python/cap07_percorsi.py
"""
f = lambda x, y: x * y / (x**2 + y**2)
g = lambda x, y: x**2 * y / (x**4 + y**2)

print("   t      f(t,0)  f(t,t)  f(t,2t)"
      "    g(t,t)  g(t,3t)  g(t,t^2)")
for t in (0.1, 0.01, 0.001, 0.0001):
    print(f"{t:7.4f}  {f(t, 0):6.3f}  {f(t, t):6.3f}"
          f"  {f(t, 2*t):6.3f}   {g(t, t):7.4f}"
          f"  {g(t, 3*t):7.4f}  {g(t, t**2):7.4f}")

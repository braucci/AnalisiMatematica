"""
fig_radice.py — codice del capitolo 1 (05-funzioni).
Eseguire dalla cartella Libro/:  python3 python/fig_radice.py
"""
# Il calcolatore disegna i grafici proprio "per punti": sceglie
# molti valori di x, calcola f(x) e unisce i punti con segmenti.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 200)          # 200 valori di x tra 0 e 5
y = np.sqrt(x)                      # f(x) = radice di x, su tutti

fig, ax = plt.subplots(figsize=(4, 3))
ax.plot(x, y, color="#1F4E79", lw=1.5, label=r"$y=\sqrt{x}$")
ax.plot([0, 1, 4], [0, 1, 2], "o", color="#B4662F")  # punti facili
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("figure/radice.png", dpi=220)

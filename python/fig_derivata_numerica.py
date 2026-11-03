"""
fig_derivata_numerica.py — Capitolo 5, errore delle derivate numeriche al variare di h.
Eseguire dalla cartella Libro/:  python3 python/fig_derivata_numerica.py
"""
import numpy as np
import matplotlib.pyplot as plt

x, esatta = 1.0, np.cos(1.0)
h = np.logspace(-15, -1, 300)
avanti = np.abs((np.sin(x + h) - np.sin(x)) / h - esatta)
centrata = np.abs((np.sin(x + h) - np.sin(x - h)) / (2 * h) - esatta)
avanti[avanti == 0] = np.nan; centrata[centrata == 0] = np.nan

fig, ax = plt.subplots(figsize=(7, 3.6))
ax.loglog(h, avanti, color="#1F4E79", lw=1.3, label="differenza in avanti")
ax.loglog(h, centrata, color="#B4662F", lw=1.3, label="differenza centrata")
ax.loglog(h, 0.5 * np.sin(1) * h, "--", color="#1F4E79", lw=0.9, alpha=0.7)
ax.loglog(h, np.cos(1) / 6 * h**2, "--", color="#B4662F", lw=0.9, alpha=0.7)
ax.loglog(h, 1.1e-16 / h, ":", color="#5A5A5A", lw=1)
ax.text(3e-12, 5e-2, r"arrotondamento $\sim\varepsilon/h$", fontsize=9, color="#5A5A5A")
ax.text(2e-4, 1.5e-10, r"troncamento $\sim h^2$", fontsize=9, color="#B4662F")
ax.text(1e-6, 3e-4, r"troncamento $\sim h$", fontsize=9, color="#1F4E79")
ax.set_xlabel(r"$h$"); ax.set_ylabel("errore assoluto")
ax.set_ylim(1e-12, 1); ax.legend(frameon=False, loc="lower left")
ax.grid(alpha=0.25, which="both", lw=0.4)
fig.tight_layout()
fig.savefig("figure/derivata_numerica.png", dpi=220)

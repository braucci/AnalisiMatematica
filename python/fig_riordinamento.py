"""
fig_riordinamento.py — Capitolo 11, la serie armonica alternata e il
suo riordinamento con due termini positivi e uno negativo.
Eseguire dalla cartella Libro/:  python3 python/fig_riordinamento.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
N = 60
orig = np.cumsum([(-1.0)**(k - 1) / k for k in range(1, N + 1)])
termini, p, q = [], 1, 2
while len(termini) < N:
    termini += [1 / p, 1 / (p + 2), -1 / q]
    p, q = p + 4, q + 2
riord = np.cumsum(termini[:N])
k = np.arange(1, N + 1)
fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.plot(k, orig, "-o", color=blu, ms=2.5, lw=0.8, label="ordine usuale")
ax.plot(k, riord, "-s", color=rame, ms=2.5, lw=0.8,
        label="due positivi, un negativo")
ax.plot([0, N + 0.5], [np.log(2)] * 2, color=blu, lw=0.8, ls="--")
ax.plot([0, N + 0.5], [1.5 * np.log(2)] * 2, color=rame, lw=0.8,
        ls="--")
ax.text(N + 1.5, np.log(2), r"$\log 2$", va="center", fontsize=9)
ax.text(N + 1.5, 1.5 * np.log(2), r"$\frac{3}{2}\log 2$", va="center",
        fontsize=9)
ax.set_xlim(0, N + 10)
ax.set_xlabel("numero di termini", fontsize=9)
ax.legend(fontsize=8, frameon=False, loc="center right",
          bbox_to_anchor=(0.88, 0.42))
ax.tick_params(labelsize=8)
for sp_ in ("top", "right"):
    ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/riordinamento.png", dpi=220)

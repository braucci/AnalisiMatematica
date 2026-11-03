"""
fig_taylor_seno.py — Capitolo 6, i polinomi di Taylor di sen x di grado 1, 3, ..., 23.
Eseguire dalla cartella Libro/:  python3 python/fig_taylor_seno.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
x = np.linspace(-1.2, 12.5, 4000)

def taylor_seno(x, n):
    """Polinomio di Taylor di sen x di grado n (dispari) in x0 = 0."""
    return sum((-1)**k * x**(2*k + 1) / math.factorial(2*k + 1)
               for k in range((n - 1) // 2 + 1))

fig, ax = plt.subplots(figsize=(8.2, 3.6))
for n in range(1, 24, 2):
    y = taylor_seno(x, n)
    ax.plot(x, y, color=rame, lw=0.8)
    # etichetta nel punto in cui il grafico esce dalla finestra |y| <= 3
    fuori = np.nonzero((np.abs(y) > 3) & (x > 0))[0]
    if len(fuori):
        i = fuori[0]
        yl = 2.65 if y[i] > 0 else -2.9
        ax.text(x[i] + 0.12, yl, str(n), color=rame, fontsize=7.5)
ax.plot(x, np.sin(x), color=blu, lw=2.0, label=r"$\mathrm{sen}\,x$")
ax.set_xlim(-1.2, 12.5); ax.set_ylim(-3, 3)
ax.axhline(0, color="black", lw=0.6); ax.axvline(0, color="black", lw=0.6)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.set_xticks([np.pi / 2 * k for k in range(0, 8)])
ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$",
                    r"$5\pi/2$", r"$3\pi$", r"$7\pi/2$"])
ax.tick_params(labelsize=8)
ax.legend(loc="lower left", fontsize=9, frameon=False)
fig.tight_layout()
fig.savefig("figure/taylor_seno.png", dpi=220)

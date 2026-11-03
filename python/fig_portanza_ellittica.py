"""
fig_portanza_ellittica.py — Capitolo 8, pianta ellittica e distribuzione della portanza.
Eseguire dalla cartella Libro/:  python3 python/fig_portanza_ellittica.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
b, W = 10.0, 10000.0
l0 = 4 * W / (np.pi * b)
l = lambda y: l0 * np.sqrt(np.clip(1 - (2 * y / b)**2, 0, None))
y = np.linspace(-b / 2, b / 2, 400)

fig, axs = plt.subplots(2, 1, figsize=(8.6, 4.6), height_ratios=(1, 1.6))
ax = axs[0]                                  # pianta: linea dei quarti di corda dritta
c0 = 1.6
c = c0 * np.sqrt(np.clip(1 - (2 * y / b)**2, 0, None))
ax.fill_between(y, 0.25 * c, -0.75 * c, color="#C9D7E8")
ax.plot(y, 0.25 * c, color=blu, lw=1.2); ax.plot(y, -0.75 * c, color=blu, lw=1.2)
ax.axhline(0, color=grigio, lw=0.6, ls="--")
ax.set_aspect("equal"); ax.set_xlim(-5.4, 5.4); ax.axis("off")
ax.set_title("pianta ellittica (apertura $b=10$ m)", fontsize=9)
ax = axs[1]
n = 10
yk = np.linspace(-b / 2, b / 2, n + 1)
for a, d in zip(yk[:-1], yk[1:]):
    lo, hi = sorted((l(a), l(d)))
    ax.add_patch(Rectangle((a, 0), d - a, lo, fc="#C9D7E8", ec=blu, lw=0.6))
    ax.add_patch(Rectangle((a, 0), d - a, hi, fill=False, ec=rame, lw=1.0))
ax.plot(y, l(y), color=blu, lw=1.6)
ax.set_xlim(-5.4, 5.4); ax.set_ylim(0, 1450)
ax.set_xlabel("$y$ [m]", fontsize=8); ax.set_ylabel("$l(y)$ [N/m]", fontsize=8)
ax.tick_params(labelsize=7)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/portanza_ellittica.png", dpi=220)

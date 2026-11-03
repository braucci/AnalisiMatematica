"""
fig_taylor_arctg.py — Capitolo 10, l'arcotangente e i suoi polinomi
di Taylor in 0 di grado 1, 3, ..., 15.
Eseguire dalla cartella Libro/:  python3 python/fig_taylor_arctg.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
x = np.linspace(-2.2, 2.2, 1000)
fig, ax = plt.subplots(figsize=(6.0, 3.3))
gradi = range(1, 16, 2)
r0, r1 = np.array(to_rgb("#F0C9A8")), np.array(to_rgb("#6E3A14"))
for i, g in enumerate(gradi):
    n = (g - 1) // 2
    T = sum((-1)**k * x**(2*k + 1) / (2*k + 1) for k in range(n + 1))
    col = r0 + (r1 - r0) * i / (len(gradi) - 1)
    ax.plot(x, T, color=col, lw=1.0)
ax.plot(x, np.arctan(x), color=blu, lw=2.0)
for v in (-1, 1):
    ax.axvline(v, color=grigio, lw=0.7, ls=":")
ax.axhline(0, color=grigio, lw=0.6)
ax.axvline(0, color=grigio, lw=0.6)
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.6, 2.6)
ax.text(1.55, 1.25, r"$\mathrm{arctg}\,x$", color=blu, fontsize=9)
ax.tick_params(labelsize=8)
for sp_ in ("top", "right"):
    ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/taylor_arctg.png", dpi=220)

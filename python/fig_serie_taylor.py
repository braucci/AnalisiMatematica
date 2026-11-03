"""
fig_serie_taylor.py — Capitolo 11, somme parziali della serie di
log(1+x) e la funzione di Cauchy exp(-1/x^2).
Eseguire dalla cartella Libro/:  python3 python/fig_serie_taylor.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.2))
x = np.linspace(-0.99, 1.6, 600)
gradi = range(2, 17, 2)
r0, r1 = np.array(to_rgb("#F0C9A8")), np.array(to_rgb("#6E3A14"))
for i, g in enumerate(gradi):
    T = sum((-1)**(k - 1) * x**k / k for k in range(1, g + 1))
    a1.plot(x, T, color=r0 + (r1 - r0) * i / (len(gradi) - 1), lw=0.9)
a1.plot(x, np.log1p(x), color=blu, lw=2.0)
a1.axvline(1, color=grigio, lw=0.7, ls=":")
a1.axvline(-1, color=grigio, lw=0.7, ls=":")
a1.set_ylim(-3, 2)
a1.set_xlim(-1.1, 1.6)
a1.set_title(r"$\log(1+x)$ e la sua serie", fontsize=9)
t = np.linspace(-2.5, 2.5, 1001)
f = np.where(t == 0, 0.0, np.exp(-1 / np.where(t == 0, 1, t)**2))
a2.plot(t, f, color=blu, lw=1.8)
a2.axhline(0, color=rame, lw=1.2, ls="--")
a2.text(0, 0.36, "polinomi di\nMac Laurin:\ntutti nulli",
        color=rame, fontsize=8, ha="center", va="center")
a2.set_ylim(-0.1, 0.9)
a2.set_title(r"$e^{-1/x^2}$", fontsize=9)
for ax in (a1, a2):
    ax.axhline(0, color=grigio, lw=0.5)
    ax.tick_params(labelsize=8)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/serie_taylor.png", dpi=220)

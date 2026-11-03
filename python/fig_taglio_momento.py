"""
fig_taglio_momento.py — Capitolo 9, carico, taglio e momento lungo la semiala.
Eseguire dalla cartella Libro/:  python3 python/fig_taglio_momento.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
W, b = 10000.0, 10.0
s, l0 = b / 2, 4 * W / (np.pi * b)
y = np.linspace(0, s, 400)
u = y / s
l_ell = l0 * np.sqrt(1 - u**2)
T_ell = l0 * s / 2 * (np.pi / 2 - np.arcsin(u) - u * np.sqrt(1 - u**2))
M_ell = l0 * s**2 * ((1 - u**2)**1.5 / 3
                     - u / 2 * (np.pi / 2 - np.arcsin(u) - u * np.sqrt(1 - u**2)))
l_uni = np.full_like(y, W / b)
T_uni = W / b * (s - y)
M_uni = W / (2 * b) * (s - y)**2

fig, axs = plt.subplots(1, 3, figsize=(8.6, 3.0))
dati = ((l_ell, l_uni, "carico $l(y)$ [N/m]"),
        (T_ell, T_uni, "taglio $T(y)$ [N]"),
        (M_ell, M_uni, "momento $M(y)$ [N m]"))
for ax, (a, c, tit) in zip(axs, dati):
    ax.plot(y, a, color=blu, lw=1.6, label="ellittico")
    ax.plot(y, c, color=rame, lw=1.2, ls="--", label="uniforme")
    ax.set_title(tit, fontsize=9)
    ax.set_xlabel("$y$ [m]", fontsize=8)
    ax.set_ylim(bottom=0)
    ax.tick_params(labelsize=7)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
axs[0].legend(fontsize=7, frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig("figure/taglio_momento.png", dpi=220)

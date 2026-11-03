"""
fig_somme_parziali.py — Capitolo 11, somme parziali della serie di
Mengoli, della serie telescopica con le radici e della serie (-1)^k.
Eseguire dalla cartella Libro/:  python3 python/fig_somme_parziali.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
n = np.arange(1, 41)
casi = (
    (n / (n + 1), 1.0, r"Mengoli: $s_n=\frac{n}{n+1}$"),
    (np.sqrt(n + 1) - 1, None, r"$\sum \frac{1}{\sqrt{k+1}+\sqrt{k}}$"),
    (np.where(n % 2 == 1, -1.0, 0.0), None, r"$\sum (-1)^k$"),
)
fig, axs = plt.subplots(1, 3, figsize=(8.6, 2.8))
for ax, (s, lim, tit) in zip(axs, casi):
    ax.plot(n, s, "o", color=blu, ms=3)
    if lim is not None:
        ax.axhline(lim, color=rame, lw=1.0, ls="--")
    ax.set_title(tit, fontsize=9)
    ax.set_xlabel("$n$", fontsize=8)
    ax.tick_params(labelsize=7)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
axs[2].set_ylim(-1.4, 0.4)
fig.tight_layout()
fig.savefig("figure/somme_parziali.png", dpi=220)

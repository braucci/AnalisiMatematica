"""
fig_esaustione.py — Capitolo 8, la differenza S_n - s_n per x^2 in [0, 1].
Eseguire dalla cartella Libro/:  python3 python/fig_esaustione.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
toni = (rame, "#D9A57E")                  # due toni per distinguere i pezzi
fig, axs = plt.subplots(1, 3, figsize=(8.6, 3.0))
for ax, n in zip(axs, (4, 8, 16)):
    x = np.linspace(0, 1, n + 1)
    x0 = 1.12                              # colonna in cui si impilano i pezzi
    for k in range(1, n + 1):
        a, b = x[k - 1], x[k]
        ax.add_patch(Rectangle((a, 0), b - a, a**2, fc="#C9D7E8", ec=blu, lw=0.5))
        c = toni[k % 2]
        ax.add_patch(Rectangle((a, a**2), b - a, b**2 - a**2, fc=c, ec="none"))
        ax.add_patch(Rectangle((x0, a**2), 1 / n, b**2 - a**2, fc=c, ec="none"))
    ax.add_patch(Rectangle((x0, 0), 1 / n, 1, fill=False, ec=grigio, ls="--", lw=0.8))
    t = np.linspace(0, 1, 200)
    ax.plot(t, t**2, color=blu, lw=1.4)
    ax.annotate("", xy=(x0 - 0.01, 0.5), xytext=(1.0, 0.5),
                arrowprops=dict(arrowstyle="->", color=grigio, lw=0.7))
    ax.set_title(f"$n={n}$:  $S_n-s_n=b^3/{n}$", fontsize=9)
    ax.set_xlim(-0.02, 1.42); ax.set_ylim(0, 1.05)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$b$"])
    ax.set_yticks([1]); ax.set_yticklabels(["$b^2$"])
    ax.tick_params(labelsize=7)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/esaustione.png", dpi=220)

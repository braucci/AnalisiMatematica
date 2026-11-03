"""
fig_discontinuita.py — Capitolo 4, i tre tipi di discontinuità.
Eseguire dalla cartella Libro/:  python3 python/fig_discontinuita.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
fig, axs = plt.subplots(1, 3, figsize=(8.4, 2.8))

# (a) eliminabile: sen x / x, con il valore 1/2 in x = 0
ax = axs[0]
for x in (np.linspace(-9, -1e-3, 400), np.linspace(1e-3, 9, 400)):
    ax.plot(x, np.sin(x) / x, color=blu, lw=1.6)
ax.plot([0], [1], "o", mfc="white", mec=blu, ms=6, zorder=3)
ax.plot([0], [0.5], "o", color=rame, ms=6, zorder=3)
ax.set_title("(a) eliminabile", fontsize=10); ax.set_ylim(-0.4, 1.25)

# (b) prima specie: salto in x = 0
ax = axs[1]
xs = np.linspace(-2, 0, 50); xd = np.linspace(0, 2, 50)
ax.plot(xs, xs / 2 - 0.5, color=blu, lw=1.6)
ax.plot(xd, xd / 2 + 1, color=blu, lw=1.6)
ax.plot([0], [-0.5], "o", mfc="white", mec=blu, ms=6, zorder=3)
ax.plot([0], [1], "o", color=rame, ms=6, zorder=3)
ax.annotate("", xy=(0.15, 1), xytext=(0.15, -0.5),
            arrowprops=dict(arrowstyle="<->", color=grigio, lw=1))
ax.text(0.25, 0.2, "salto", fontsize=9, color=grigio)
ax.set_title("(b) prima specie", fontsize=10); ax.set_ylim(-1.7, 2.2)

# (c) seconda specie: e^(1/x) (limite sinistro 0, limite destro +infinito)
ax = axs[2]
xs = np.linspace(-2.5, -1e-3, 400); xd = np.linspace(0.13, 2.5, 400)
ax.plot(xs, np.exp(1 / xs), color=blu, lw=1.6)
ax.plot(xd, np.exp(1 / xd), color=blu, lw=1.6)
ax.plot([0], [0], "o", mfc="white", mec=blu, ms=6, zorder=3)
ax.set_title(r"(c) seconda specie: $e^{1/x}$", fontsize=10); ax.set_ylim(-0.5, 2200)
ax.set_yscale("symlog", linthresh=1)
ax.set_yticks([0, 1, 10, 100, 1000]); ax.set_yticklabels(["0", "1", "10", "100", "1000"])

for ax in axs:
    ax.axhline(0, color="black", lw=0.6); ax.axvline(0, color="black", lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)
fig.tight_layout()
fig.savefig("figure/discontinuita.png", dpi=220)

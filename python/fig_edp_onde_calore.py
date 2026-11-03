"""
fig_edp_onde_calore.py — Capitolo 7, un primo sguardo alle equazioni alle
derivate parziali: la soluzione di d'Alembert dell'equazione delle onde e la
soluzione gaussiana dell'equazione del calore.
Eseguire dalla cartella Libro/:  python3 python/fig_edp_onde_calore.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio, verde = "#1F4E79", "#B4662F", "#5A5A5A", "#2F6B4F"
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.3))

# (a) onde: u(x,t) = [F(x - ct) + F(x + ct)] / 2, con F(x) = exp(-4 x^2), c = 1
F = lambda s: np.exp(-4 * s**2)
x = np.linspace(-5, 5, 801)
ax = axs[0]
for tt, col in ((0.0, blu), (1.5, rame), (3.0, verde)):
    ax.plot(x, 0.5 * (F(x - tt) + F(x + tt)), color=col, lw=1.5,
            label=f"$t={tt:g}$".replace(".", "{,}"))
for s in (-1, 1):                          # le due onde viaggiano a velocità c
    ax.annotate("", xy=(s * 4.2, 0.58), xytext=(s * 3.0, 0.58),
                arrowprops=dict(arrowstyle="->", color=grigio, lw=0.9))
ax.text(0, 1.08, r"$u=\frac{1}{2}\,[F(x-ct)+F(x+ct)]$", ha="center",
        fontsize=8)
ax.set_ylim(-0.05, 1.2)
ax.set_title(r"onde: $u_{tt}=c^{2}u_{xx}$, con $c=1$", fontsize=9)
ax.legend(fontsize=7, frameon=False, loc="upper right")

# (b) calore: u(x,t) = exp(-x^2 / (4kt)) / sqrt(4 pi k t), con k = 1
x = np.linspace(-4, 4, 801)
ax = axs[1]
for tt, col in ((0.05, blu), (0.2, rame), (1.0, verde)):
    u = np.exp(-x**2 / (4 * tt)) / np.sqrt(4 * np.pi * tt)
    ax.plot(x, u, color=col, lw=1.5,
            label=f"$t={tt:g}$".replace(".", "{,}"))
ax.set_ylim(-0.05, 1.4)
ax.set_title(r"calore: $u_{t}=k\,u_{xx}$, con $k=1$", fontsize=9)
ax.legend(fontsize=7, frameon=False, loc="upper right")

for ax in axs:
    ax.set_xlabel("$x$", fontsize=8)
    ax.set_ylabel("$u(x,t)$", fontsize=8)
    ax.tick_params(labelsize=7)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/edp_onde_calore.png", dpi=220)

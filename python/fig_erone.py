"""
fig_erone.py — Capitolo 3, diagramma a ragnatela del metodo di Erone per sqrt(2).
Eseguire dalla cartella Libro/:  python3 python/fig_erone.py
"""
import numpy as np
import matplotlib.pyplot as plt

g = lambda x: 0.5 * (x + 2 / x)
x = np.linspace(0.9, 3.2, 400)

fig, ax = plt.subplots(figsize=(5, 4.2))
ax.plot(x, g(x), color="#1F4E79", lw=1.6, label=r"$y=\frac{1}{2}\left(x+\frac{2}{x}\right)$")
ax.plot(x, x, color="#5A5A5A", lw=1, ls="--", label=r"$y=x$")
xn = 3.0
for _ in range(5):                     # la ragnatela: verticale poi orizzontale
    yn = g(xn)
    ax.plot([xn, xn], [xn, yn], color="#B4662F", lw=1)
    ax.plot([xn, yn], [yn, yn], color="#B4662F", lw=1)
    xn = yn
ax.plot([np.sqrt(2)], [np.sqrt(2)], "o", color="#2F6B4F", ms=6)
ax.annotate(r"$\sqrt{2}$", (np.sqrt(2), np.sqrt(2)), xytext=(1.0, 1.75),
            arrowprops=dict(arrowstyle="->", color="#2F6B4F"), color="#2F6B4F")
ax.set_xlim(0.9, 3.2); ax.set_ylim(0.9, 3.2); ax.set_aspect("equal")
ax.legend(frameon=False, loc="upper left")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/erone.png", dpi=220)

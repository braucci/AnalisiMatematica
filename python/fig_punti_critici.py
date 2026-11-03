"""
fig_punti_critici.py — Capitolo 7, punti critici: curve di livello di x^3-6y(x+y)
e grafico di y exp(-(x^2+y^2)).
Eseguire dalla cartella Libro/:  python3 python/fig_punti_critici.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
mappa = LinearSegmentedColormap.from_list("libro", [blu, "#E8EEF4", rame])
fig = plt.figure(figsize=(8.6, 3.9))

ax = fig.add_subplot(1, 2, 1)
x = np.linspace(-2.4, 1.4, 400)
y = np.linspace(-1.4, 1.6, 400)
X, Y = np.meshgrid(x, y)
Z = X**3 - 6 * Y * (X + Y)
livelli = sorted(set(np.arange(-6, 1.6, 0.5)) | {0.2, 0.35, 0.45})
cs = ax.contour(X, Y, Z, levels=livelli, cmap=mappa, linewidths=0.8)
ax.contour(X, Y, Z, levels=[0], colors=grigio, linewidths=1.1)
ax.plot([-1], [0.5], "o", color=rame, ms=5)
ax.plot([0], [0], "s", color=blu, ms=5)
box = dict(boxstyle="round,pad=0.15", fc="white", ec="none")
ax.annotate("massimo $(-1,1/2)$", (-1, 0.5), (-2.3, 1.25), fontsize=8, bbox=box,
            color=rame, arrowprops=dict(arrowstyle="-", color=rame, lw=0.6))
ax.annotate("sella $(0,0)$", (0, 0), (0.25, -1.15), fontsize=8, color=blu,
            bbox=box, arrowprops=dict(arrowstyle="-", color=blu, lw=0.6))
ax.set_title(r"curve di livello di $x^3-6y(x+y)$", fontsize=9)
ax.set_xlabel("$x$", fontsize=8); ax.set_ylabel("$y$", fontsize=8)
ax.set_aspect("equal"); ax.tick_params(labelsize=7)

ax = fig.add_subplot(1, 2, 2, projection="3d", computed_zorder=False)
u = np.linspace(-2.2, 2.2, 121)
X, Y = np.meshgrid(u, u)
ax.plot_surface(X, Y, Y * np.exp(-(X**2 + Y**2)), cmap=mappa, rcount=45,
                ccount=45, linewidth=0.12, edgecolor=grigio, alpha=0.95, zorder=1)
s = np.sqrt(2) / 2
for yy, col in ((s, rame), (-s, blu)):
    ax.scatter([0], [yy], [yy * np.exp(-0.5)], color=col, s=18,
               depthshade=False, zorder=5)
ax.set_title(r"$z=y\,e^{-(x^2+y^2)}$", fontsize=9)
ax.set_xlabel("$x$", fontsize=8, labelpad=-8)
ax.set_ylabel("$y$", fontsize=8, labelpad=-8)
for asse in (ax.xaxis, ax.yaxis, ax.zaxis):
    asse.set_major_locator(plt.MaxNLocator(3))
ax.tick_params(labelsize=6, pad=-3)
ax.view_init(elev=24, azim=-60)
fig.tight_layout()
fig.savefig("figure/punti_critici.png", dpi=220, bbox_inches="tight", pad_inches=0.04)

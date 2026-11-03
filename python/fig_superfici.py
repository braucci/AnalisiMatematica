"""
fig_superfici.py — Capitolo 7, grafici di quattro funzioni di due variabili.
Eseguire dalla cartella Libro/:  python3 python/fig_superfici.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

mappa = LinearSegmentedColormap.from_list("libro", ["#1F4E79", "#E8EEF4", "#B4662F"])

def griglia_quadrata(L, n=161):
    u = np.linspace(-L, L, n)
    return np.meshgrid(u, u)

def griglia_disco(R, n=161):
    r, t = np.meshgrid(np.linspace(0, R, n), np.linspace(0, 2 * np.pi, n))
    return r * np.cos(t), r * np.sin(t)

casi = [
    (r"$z=x^2-y^2$ (paraboloide iperbolico)", lambda x, y: x**2 - y**2, griglia_quadrata(1.0), 28),
    (r"$z=y\,(x^2+x)$ (superficie rigata)", lambda x, y: y * (x**2 + x), griglia_quadrata(1.0), 28),
    (r"$z=\cos(x^2+y^2)$", lambda x, y: np.cos(x**2 + y**2), griglia_disco(3.0), 52),
    (r"$z=\mathrm{sen}\,(xy)$", lambda x, y: np.sin(x * y), griglia_quadrata(2.6), 28),
]
fig = plt.figure(figsize=(8.6, 7.2))
for i, (titolo, f, (X, Y), elev) in enumerate(casi):
    ax = fig.add_subplot(2, 2, i + 1, projection="3d")
    ax.plot_surface(X, Y, f(X, Y), cmap=mappa, rcount=70, ccount=70,
                    linewidth=0.12, edgecolor="#5A5A5A", alpha=0.97)
    ax.set_title(titolo, fontsize=9)
    ax.set_xlabel("$x$", fontsize=8, labelpad=-8)
    ax.set_ylabel("$y$", fontsize=8, labelpad=-8)
    for asse in (ax.xaxis, ax.yaxis, ax.zaxis):
        asse.set_major_locator(plt.MaxNLocator(3))
    ax.tick_params(labelsize=6, pad=-3)
    ax.view_init(elev=elev, azim=-55)
fig.tight_layout()
fig.savefig("figure/superfici.png", dpi=220, bbox_inches="tight", pad_inches=0.04)

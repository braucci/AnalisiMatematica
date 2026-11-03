"""
fig_radiali.py — Capitolo 7, funzioni invarianti per rotazioni e loro domini.
Eseguire dalla cartella Libro/:  python3 python/fig_radiali.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

mappa = LinearSegmentedColormap.from_list("libro", ["#1F4E79", "#E8EEF4", "#B4662F"])

def corona(r1, r2, n=121):
    """Griglia polare sulla corona circolare r1 <= r <= r2."""
    r, t = np.meshgrid(np.linspace(r1, r2, n), np.linspace(0, 2 * np.pi, n))
    return r * np.cos(t), r * np.sin(t)

casi = [
    (r"$z=\log(x^2+y^2)$", lambda x, y: np.log(x**2 + y**2), corona(0.08, 2.0)),
    (r"$z=1-\sqrt{x^2+y^2}$", lambda x, y: 1 - np.sqrt(x**2 + y**2), corona(0.0, 2.0)),
    (r"$z=1-\sqrt{x^2+y^2-1}$", lambda x, y: 1 - np.sqrt(np.maximum(x**2 + y**2 - 1, 0)), corona(1.0, 2.2)),
    (r"$z=1-\sqrt{x^2+y^2-2}$", lambda x, y: 1 - np.sqrt(np.maximum(x**2 + y**2 - 2, 0)), corona(np.sqrt(2), 2.4)),
]
fig = plt.figure(figsize=(8.6, 7.0))
for i, (titolo, f, (X, Y)) in enumerate(casi):
    ax = fig.add_subplot(2, 2, i + 1, projection="3d")
    ax.plot_surface(X, Y, f(X, Y), cmap=mappa, rcount=50, ccount=60,
                    linewidth=0.12, edgecolor="#5A5A5A", alpha=0.97)
    ax.set_title(titolo, fontsize=9)
    ax.set_xlabel("$x$", fontsize=8, labelpad=-8)
    ax.set_ylabel("$y$", fontsize=8, labelpad=-8)
    for asse in (ax.xaxis, ax.yaxis, ax.zaxis):
        asse.set_major_locator(plt.MaxNLocator(3))
    ax.tick_params(labelsize=6, pad=-3)
    ax.view_init(elev=24, azim=-55)
fig.tight_layout()
fig.savefig("figure/radiali.png", dpi=220, bbox_inches="tight", pad_inches=0.04)

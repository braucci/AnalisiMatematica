"""
fig_uniforme.py — Capitolo 8, uniforme continuità: x^2 e sqrt(x).
Eseguire dalla cartella Libro/:  python3 python/fig_uniforme.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.5))
ax = axs[0]
eps = 0.5
t = np.linspace(0, 3.25, 300)
ax.plot(t, t**2, color=blu, lw=1.5)
for x0 in (0.5, 1.5, 2.8):
    d = np.sqrt(x0**2 + eps) - x0             # delta massimo, formula (delta-x2)
    ax.add_patch(Rectangle((x0 - d, x0**2 - eps), 2 * d, 2 * eps,
                           fc=rame, alpha=0.25, ec=rame, lw=1.0))
    ax.plot(x0, x0**2, "o", color=rame, ms=3)
    ax.text(x0 + d + 0.06, x0**2 - 0.35, f"$\\delta\\approx{d:.2f}$",
            fontsize=7, color=rame)
ax.set_title("$x^2$: la finestra deve restringersi", fontsize=9)
ax.set_xlim(0, 3.4); ax.set_ylim(-0.6, 10.5)
ax = axs[1]
eps = 0.4
d = eps**2
t = np.linspace(0, 4.2, 400)
ax.plot(t, np.sqrt(t), color=blu, lw=1.5)
for x0 in (d, 1.0, 2.2, 3.6):        # la prima finestra parte da x = 0
    ax.add_patch(Rectangle((x0 - d, np.sqrt(x0) - eps), 2 * d, 2 * eps,
                           fc=rame, alpha=0.25, ec=rame, lw=1.0))
    ax.plot(x0, np.sqrt(x0), "o", color=rame, ms=3)
ax.set_title(r"$\sqrt{x}$: la stessa finestra va bene ovunque", fontsize=9)
ax.set_xlim(-0.3, 4.3); ax.set_ylim(-0.5, 2.5)
for ax in axs:
    ax.tick_params(labelsize=7)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/uniforme.png", dpi=220)

"""
fig_discontinua.py — Capitolo 7, la funzione xy/(x^2+y^2): è costante su ogni retta
per l'origine, quindi vicino all'origine assume tutti i valori di [-1/2, 1/2].
Eseguire dalla cartella Libro/:  python3 python/fig_discontinua.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
mappa = LinearSegmentedColormap.from_list("libro", [blu, "#D9DEE4", rame])
fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.6),
                        gridspec_kw={"width_ratios": [1, 1.25]})
ax = axs[0]                                # curve di livello: semirette
for th in np.linspace(0, 2 * np.pi, 49)[:-1]:
    v = 0.5 * np.sin(2 * th)
    ax.plot([0, np.cos(th)], [0, np.sin(th)], color=mappa(v + 0.5), lw=1.4)
ax.add_patch(plt.Circle((0, 0), 0.35, fill=False, ls="--", color=grigio, lw=0.8))
ax.text(0.72, 0.8, r"$f=\frac{1}{2}$", color=rame, fontsize=9)
ax.text(0.72, -0.9, r"$f=-\frac{1}{2}$", color=blu, fontsize=9)
ax.text(1.03, 0.04, r"$f=0$", color=grigio, fontsize=8)
ax.set_aspect("equal"); ax.set_xlim(-1.1, 1.35); ax.set_ylim(-1.1, 1.1)
ax.set_title("curve di livello: semirette per l'origine", fontsize=9)
ax.tick_params(labelsize=7)
ax = axs[1]                                # valore in funzione dell'angolo
th = np.linspace(0, 2 * np.pi, 400)
ax.plot(th, 0.5 * np.sin(2 * th), color=blu, lw=1.5)
ax.axhline(0, color="black", lw=0.6)
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
ax.set_xlabel(r"angolo $\vartheta$ della semiretta", fontsize=8)
ax.set_title(r"$f(\rho\cos\vartheta,\rho\,\mathrm{sen}\,\vartheta)="
             r"\frac{1}{2}\,\mathrm{sen}\,2\vartheta$", fontsize=9)
ax.tick_params(labelsize=7)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/discontinua.png", dpi=220)

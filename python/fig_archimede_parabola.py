"""
fig_archimede_parabola.py — Capitolo 8, la quadratura della parabola di Archimede:
il triangolo di Archimede e le prime generazioni di triangoli inscritti.
Eseguire dalla cartella Libro/:  python3 python/fig_archimede_parabola.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

blu, rame, grigio, verde = "#1F4E79", "#B4662F", "#5A5A5A", "#2F6B4F"
chiaro = "#C9D7E8"
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.6))

# --- a sinistra: il triangolo di Archimede e il parallelogramma -----------
ax = axs[0]
p, r = -0.3, 1.3
q = (p + r) / 2
corda = lambda x: (p + r) * x - p * r          # retta AB
paral = lambda x: (p + r) * x - q**2           # retta per C parallela ad AB
x = np.linspace(p, r, 200)
ax.fill_between(x, x**2, corda(x), color=chiaro, lw=0)
par = [(p, corda(p)), (r, corda(r)), (r, paral(r)), (p, paral(p))]
ax.add_patch(Polygon(par, closed=True, fill=False, ec=grigio, ls="--",
                     lw=0.9))
A, B, C = (p, p**2), (r, r**2), (q, q**2)
ax.add_patch(Polygon([A, B, C], closed=True, fc=blu, alpha=0.30, ec=blu,
                     lw=1.0))
t = np.linspace(-0.45, 1.42, 300)
ax.plot(t, t**2, color=blu, lw=1.5)
ax.plot([q, q], [q**2, corda(q)], color=rame, lw=1.3)
for P, nome, dx, dy in ((A, "$A$", -0.09, 0.02), (B, "$B$", 0.04, -0.06),
                        (C, "$C$", 0.03, -0.17), ((q, corda(q)), "$D$",
                                                  -0.1, 0.07)):
    ax.plot(*P, "o", color=blu if nome != "$D$" else rame, ms=3)
    ax.text(P[0] + dx, P[1] + dy, nome, fontsize=10.5)
ax.text(q + 0.04, (q**2 + corda(q)) / 2 - 0.05, "$d$", fontsize=10.5,
        color=rame)
ax.text(1.0, 0.36, "tangente in $C$", fontsize=7.5, color=grigio,
        rotation=26)
ax.set_title("il triangolo di Archimede e il parallelogramma", fontsize=9)
ax.set_xlim(-0.5, 1.5); ax.set_ylim(-0.62, 1.8)
ax.set_xticks([p, q, r]); ax.set_xticklabels(["$p$", "$q$", "$r$"])
ax.set_yticks([])

# --- a destra: le generazioni di triangoli inscritti --------------------
ax = axs[1]
colori = (blu, rame, verde)
etichette = ("generazione 0: $T$", "generazione 1: $2\\cdot T/8$",
             "generazione 2: $4\\cdot T/64$")
for k, (col, lab) in enumerate(zip(colori, etichette)):
    nodi = np.linspace(-1, 1, 2**k + 1)
    for a, b in zip(nodi[:-1], nodi[1:]):
        m = (a + b) / 2
        tri = [(a, a**2), (b, b**2), (m, m**2)]
        ax.add_patch(Polygon(tri, closed=True, fc=col, alpha=0.32, ec=col,
                             lw=0.8, label=lab if a == -1 else None))
t = np.linspace(-1.08, 1.08, 300)
ax.plot(t, t**2, color=blu, lw=1.5)
ax.plot([-1, 1], [1, 1], color=grigio, lw=0.9)
ax.legend(loc="upper center", fontsize=8.5, frameon=False, ncol=1,
          bbox_to_anchor=(0.5, 1.02))
ax.set_title("le prime tre generazioni di triangoli", fontsize=9)
ax.set_xlim(-1.12, 1.12); ax.set_ylim(-0.05, 1.62)
ax.set_xticks([-1, 0, 1]); ax.set_yticks([])
for a in axs:
    a.tick_params(labelsize=7.5)
    for s in ("top", "right", "left"):
        a.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/archimede_parabola.png", dpi=220)

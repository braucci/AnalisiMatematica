"""
fig_minimi_quadrati.py — Capitolo 7, la polare parabolica stimata con i minimi quadrati.
Eseguire dalla cartella Libro/:  python3 python/fig_minimi_quadrati.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
rng = np.random.default_rng(7)            # stessi dati di python/cap07_minimi_quadrati.py
CL = np.linspace(0.0, 1.2, 13)
CD = 0.025 + 0.0497 * CL**2 + rng.normal(0, 0.0008, CL.size)
a, b = np.polyfit(CL**2, CD, 1)
t = np.linspace(0, 1.3, 200)

fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.4))
ax = axs[0]
ax.plot(CD, CL, "o", color=rame, ms=4, label="misure")
ax.plot(b + a * t**2, t, color=blu, lw=1.5, label=r"$C_D=C_{D0}+k\,C_L^2$")
ax.set_xlabel("$C_D$", fontsize=8); ax.set_ylabel("$C_L$", fontsize=8)
ax.set_title("polare: misure e modello", fontsize=9)
ax.legend(fontsize=7, frameon=False, loc="lower right")
ax = axs[1]
X = CL**2
ax.plot(X, CD, "o", color=rame, ms=4)
ax.plot(t**2, b + a * t**2, color=blu, lw=1.5)
for xi, yi in zip(X, CD):                  # residui verticali
    ax.plot([xi, xi], [yi, b + a * xi], color=grigio, lw=0.7)
ax.set_xlabel("$X=C_L^2$", fontsize=8); ax.set_ylabel("$C_D$", fontsize=8)
ax.set_title("retta dei minimi quadrati e residui", fontsize=9)
for ax in axs:
    ax.tick_params(labelsize=7)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/minimi_quadrati.png", dpi=220)

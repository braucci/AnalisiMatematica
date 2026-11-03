"""
fig_livello.py — Capitolo 7, curve di livello: isobare con il gradiente e curve di
portanza costante nel piano (V, C_L).
Eseguire dalla cartella Libro/:  python3 python/fig_livello.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.9))

# (a) campo di pressione con un'alta (A) e una bassa (B), in hPa
p = lambda x, y: 1013 + 12 * np.exp(-((x + 1.2)**2 + y**2)) \
    - 12 * np.exp(-((x - 1.2)**2 + y**2))
u = np.linspace(-3, 3, 301)
X, Y = np.meshgrid(u, u)
ax = axs[0]
cs = ax.contour(X, Y, p(X, Y), levels=np.arange(1002, 1025, 2), colors=blu,
                linewidths=0.8)
etichette = ax.clabel(cs, fmt="%d", fontsize=6)
q = np.linspace(-2.4, 2.4, 11)
QX, QY = np.meshgrid(q, q)
h = 1e-4                                   # gradiente con differenze centrate
px = (p(QX + h, QY) - p(QX - h, QY)) / (2 * h)
py = (p(QX, QY + h) - p(QX, QY - h)) / (2 * h)
ax.quiver(QX, QY, -px, -py, color=rame, scale=140, width=0.0045, zorder=2)
for t in etichette:                        # etichette leggibili sopra le frecce
    t.set_bbox(dict(facecolor="white", edgecolor="none", pad=0.6))
    t.set_zorder(3)
for xc, lettera in ((-1.2, "A"), (1.2, "B")):
    ax.text(xc, 0, lettera, ha="center", va="center", fontsize=11, color=blu,
            weight="bold", zorder=3,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.8))
ax.set_title(r"isobare e vettori $-\nabla p$", fontsize=9)
ax.set_aspect("equal")

# (b) curve di livello di L(V, C_L) = 1/2 rho S V^2 C_L
rho, S, W = 1.225, 16.0, 10000.0
V = np.linspace(20, 80, 300)
CL = np.linspace(0.05, 1.6, 300)
VV, CC = np.meshgrid(V, CL)
ax = axs[1]
livelli = [6, 8, 13, 16, 20, 25]
cs = ax.contour(VV, CC, 0.5 * rho * S * VV**2 * CC / 1000,
                levels=livelli, colors=grigio, linewidths=0.7)
pos = [(np.sqrt(2000 * L / (rho * S * 1.25)), 1.25) for L in livelli]
ax.clabel(cs, fmt="%d kN", fontsize=6, manual=pos)
ax.plot(V, 2 * W / (rho * S * V**2), color=rame, lw=1.8)
ax.annotate(r"$L=W=10$ kN", (60, 2 * W / (rho * S * 60**2)), (62, 0.95),
            color=rame, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=rame, lw=0.7))
ax.set_ylim(0, 1.6)
ax.set_xlabel("$V$ (m/s)", fontsize=8)
ax.set_ylabel("$C_L$", fontsize=8)
ax.set_title(r"curve di livello di $L(V,C_L)$", fontsize=9)
for ax in axs:
    ax.tick_params(labelsize=7)
fig.tight_layout()
fig.savefig("figure/livello.png", dpi=220)

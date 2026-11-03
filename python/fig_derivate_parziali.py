"""
fig_derivate_parziali.py — Capitolo 7, significato geometrico delle derivate parziali.
Eseguire dalla cartella Libro/:  python3 python/fig_derivate_parziali.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, verde, grigio = "#1F4E79", "#B4662F", "#2F6B4F", "#5A5A5A"
f = lambda x, y: 3 - x**2 / 2 - y**2 / 4
x0, y0 = 1.0, 1.0
z0, fx, fy = f(x0, y0), -x0, -y0 / 2

u = np.linspace(-2, 2, 81)
X, Y = np.meshgrid(u, u)
fig = plt.figure(figsize=(6.4, 5.0))
ax = fig.add_subplot(projection="3d", computed_zorder=False)
ax.plot_surface(X, Y, f(X, Y), color="#C9D6E3", rcount=30, ccount=30,
                linewidth=0.2, edgecolor="#8C9BAA", alpha=0.45, zorder=1)
# sezione con il piano y = y0 e retta tangente di pendenza f_x
ax.plot(u, np.full_like(u, y0), f(u, y0), color=rame, lw=2, zorder=5)
t = np.linspace(x0 - 1.2, x0 + 1.2, 2)
ax.plot(t, np.full_like(t, y0), z0 + fx * (t - x0), color=rame, lw=1.2, ls="--", zorder=5)
# sezione con il piano x = x0 e retta tangente di pendenza f_y
ax.plot(np.full_like(u, x0), u, f(x0, u), color=verde, lw=2, zorder=5)
t = np.linspace(y0 - 1.6, y0 + 1.6, 2)
ax.plot(np.full_like(t, x0), t, z0 + fy * (t - y0), color=verde, lw=1.2, ls="--", zorder=5)
ax.plot([x0, x0], [y0, y0], [0, z0], color=grigio, lw=0.8, ls=":", zorder=5)
ax.scatter([x0], [y0], [z0], color="black", s=12, depthshade=False, zorder=6)
ax.scatter([x0], [y0], [0], color="black", s=8, depthshade=False, zorder=6)
ax.text(x0 + 0.1, y0, 0.15, r"$(x_0,y_0)$", fontsize=8)
ax.text(2.1, y0, f(2, y0) - 0.1, r"$z=f(x,y_0)$", color=rame, fontsize=8)
ax.text(x0, -2.3, f(x0, -2) + 0.3, r"$z=f(x_0,y)$", color=verde, fontsize=8)
ax.set_xlabel("$x$", fontsize=8, labelpad=-6)
ax.set_ylabel("$y$", fontsize=8, labelpad=-6)
ax.set_zlabel("$z$", fontsize=8, labelpad=-6)
ax.set_zlim(0, 3.2)
for asse in (ax.xaxis, ax.yaxis, ax.zaxis):
    asse.set_major_locator(plt.MaxNLocator(3))
ax.tick_params(labelsize=6, pad=-3)
ax.view_init(elev=24, azim=-60)
fig.tight_layout()
fig.savefig("figure/derivate_parziali.png", dpi=220, bbox_inches="tight", pad_inches=0.04)

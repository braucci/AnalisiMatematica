"""
fig_cancellazione.py — Capitolo 10, errore relativo nel calcolo di
1/x^2 - 1/(x sen x): formula diretta contro polinomio di Taylor.
Eseguire dalla cartella Libro/:  python3 python/fig_cancellazione.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp, mpf, sin as msin

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
mp.dps = 50
xs = np.logspace(-8, 0, 400)
err_d, err_t = [], []
for t in xs:
    esatto = 1 / mpf(t)**2 - 1 / (mpf(t) * msin(mpf(t)))
    d = 1 / t**2 - 1 / (t * math.sin(t))
    p = -1 / 6 - 7 * t**2 / 360
    err_d.append(max(float(abs((d - esatto) / esatto)), 1e-17))
    err_t.append(max(float(abs((p - esatto) / esatto)), 1e-17))
fig, ax = plt.subplots(figsize=(6.0, 3.3))
ax.loglog(xs, err_d, color=blu, lw=1.0, label="formula diretta")
ax.loglog(xs, err_t, color=rame, lw=1.4,
          label=r"Taylor $-\frac{1}{6}-\frac{7x^2}{360}$")
ax.loglog(xs, 6 * 2.2e-16 / xs**2, color=grigio, lw=0.8, ls="--")
ax.text(2e-7, 3e-2, r"$\sim\varepsilon/x^2$", color=grigio, fontsize=8)
ax.set_xlim(1e-8, 1)
ax.set_ylim(1e-17, 10)
ax.set_xlabel("$x$", fontsize=9)
ax.set_ylabel("errore relativo", fontsize=9)
ax.legend(fontsize=8, frameon=False, loc="upper left",
          bbox_to_anchor=(0.36, 1.0))
ax.tick_params(labelsize=8)
for sp_ in ("top", "right"):
    ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/cancellazione.png", dpi=220)

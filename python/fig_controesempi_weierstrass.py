"""
fig_controesempi_weierstrass.py — Capitolo 4, quando il teorema di Weierstrass non si applica.
Eseguire dalla cartella Libro/:  python3 python/fig_controesempi_weierstrass.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
fig, axs = plt.subplots(2, 2, figsize=(7.6, 5.4))

# (a) 1/x su (0, 1]: non limitata, niente massimo
ax = axs[0, 0]
x = np.linspace(0.08, 1, 300)
ax.plot(x, 1 / x, color=blu, lw=1.8)
ax.plot([1], [1], "o", color=blu, ms=5)
ax.set_title(r"(a) $1/x$ su $(0,1]$: non ha massimo", fontsize=9.5)
ax.set_xlim(0, 1.6); ax.set_ylim(0, 13)

# (b) 1/x su [1, +inf): limitata, niente minimo
ax = axs[0, 1]
x = np.linspace(1, 12, 300)
ax.plot(x, 1 / x, color=blu, lw=1.8)
ax.plot([1], [1], "o", color=blu, ms=5)
ax.set_title(r"(b) $1/x$ su $[1,{+}\infty)$: non ha minimo", fontsize=9.5)
ax.set_xlim(0, 12); ax.set_ylim(-0.1, 1.3)

# (c) x^2 con g(0) = 1 su [-1, 1]: discontinua, niente minimo
ax = axs[1, 0]
x = np.linspace(-1, 1, 300)
ax.plot(x, x**2, color=blu, lw=1.8)
ax.plot([0], [0], "o", mfc="white", mec=blu, ms=6, zorder=3)
ax.plot([0], [1], "o", color=rame, ms=6, zorder=3)
ax.plot([-1, 1], [1, 1], "o", color=blu, ms=5)
ax.set_title(r"(c) $g$ su $[-1,1]$: non ha minimo", fontsize=9.5)
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-0.15, 1.25)

# (d) parte frazionaria x - floor(x) su [-2, 3]: niente massimo
ax = axs[1, 1]
for k in range(-2, 3):
    xs = np.linspace(k, k + 1, 50)
    ax.plot(xs[:-1], xs[:-1] - k, color=blu, lw=1.8)
    ax.plot([k], [0], "o", color=blu, ms=4.5, zorder=3)
    ax.plot([k + 1], [1], "o", mfc="white", mec=blu, ms=5, zorder=3)
ax.plot([3], [0], "o", color=blu, ms=4.5, zorder=3)
ax.axhline(1, color=grigio, ls="--", lw=0.8)
ax.set_title(r"(d) $x-\lfloor x\rfloor$ su $[-2,3]$: non ha massimo", fontsize=9.5)
ax.set_xlim(-2.4, 3.4); ax.set_ylim(-0.15, 1.3)

for ax in axs.flat:
    ax.axhline(0, color="black", lw=0.6); ax.axvline(0, color="black", lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=8)
fig.tight_layout()
fig.savefig("figure/controesempi_weierstrass.png", dpi=220)

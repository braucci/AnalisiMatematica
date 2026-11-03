"""
fig_taylor_composte.py — Capitolo 10, sen x^2, sen x^3, 1+sen(e^x-1)
e le loro approssimazioni vicino all'origine.
Eseguire dalla cartella Libro/:  python3 python/fig_taylor_composte.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
casi = (
    (lambda x: np.sin(x**2), lambda x: x**2, (-3.3, 3.3), (-1.4, 2.2),
     r"$\mathrm{sen}\,x^2$ e $x^2$"),
    (lambda x: np.sin(x**3), lambda x: x**3, (-2.4, 2.4), (-1.6, 1.6),
     r"$\mathrm{sen}\,x^3$ e $x^3$"),
    (lambda x: 1 + np.sin(np.exp(x) - 1), np.exp, (-4.0, 2.6),
     (-0.2, 3.0), r"$1+\mathrm{sen}\,(e^x-1)$ e $e^x$"),
)
fig, axs = plt.subplots(1, 3, figsize=(8.6, 2.9))
for ax, (f, g, (a, b), (c, d), tit) in zip(axs, casi):
    x = np.linspace(a, b, 3000)
    ax.plot(x, f(x), color=blu, lw=1.3)
    ax.plot(x, g(x), color=rame, lw=1.2, ls="--")
    ax.axhline(0, color=grigio, lw=0.6)
    ax.axvline(0, color=grigio, lw=0.6)
    ax.set_xlim(a, b)
    ax.set_ylim(c, d)
    ax.set_title(tit, fontsize=9)
    ax.tick_params(labelsize=7)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/taylor_composte.png", dpi=220)

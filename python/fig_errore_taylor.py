"""
fig_errore_taylor.py — Capitolo 10, errore dei polinomi di Taylor:
e - somme parziali contro la stima 3/(n+1)!; |sen x - T_(2n+1)(x)|.
Eseguire dalla cartella Libro/:  python3 python/fig_errore_taylor.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp, mpf, e as me, sin as msin, factorial as mfact

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
mp.dps = 40
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.2))
n = np.arange(0, 16)
R = [float(me - sum(1 / mfact(k) for k in range(m + 1))) for m in n]
S = [3 / math.factorial(m + 1) for m in n]
a1.semilogy(n, R, "o", color=blu, ms=4, label=r"$R_n(1)$")
a1.semilogy(n, S, "s", color=rame, ms=3, mfc="none",
            label=r"$3/(n+1)!$")
a1.set_xlabel("$n$", fontsize=9)
a1.legend(fontsize=8, frameon=False)
xs = np.linspace(0.01, math.pi, 300)
for i, g in enumerate((1, 3, 5, 7, 9)):
    err = []
    for t in xs:
        tm = mpf(t)
        T = sum((-1)**k * tm**(2*k+1) / mfact(2*k+1)
                for k in range((g + 1) // 2))
        err.append(float(abs(msin(tm) - T)))
    col = plt.cm.copper(0.15 + 0.17 * i)
    a2.semilogy(xs, err, color=col, lw=1.2, label=f"grado {g}")
a2.set_ylim(1e-16, 10)
a2.set_xlim(0, math.pi)
a2.set_xlabel("$x$", fontsize=9)
a2.legend(fontsize=7, frameon=False, loc="lower right")
for ax in (a1, a2):
    ax.tick_params(labelsize=8)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/errore_taylor.png", dpi=220)

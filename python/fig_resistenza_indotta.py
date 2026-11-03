"""
fig_resistenza_indotta.py — Capitolo 11, circolazione di un'ala
rettangolare (AR = 6) e somme parziali della serie di Glauert delta.
Eseguire dalla cartella Libro/:  python3 python/fig_resistenza_indotta.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
AR, N = 6.0, 12
n = np.arange(1, 2 * N, 2)
th = np.arange(1, N + 1) * np.pi / (2 * N)
mu = 2 * np.pi / (4 * AR)
M = np.sin(np.outer(th, n)) * (np.sin(th)[:, None] + n * mu)
A = np.linalg.solve(M, mu * np.sin(th))
t = np.linspace(0, np.pi, 400)
y = -np.cos(t)                                   # y / (b/2)
G = np.sin(np.outer(t, n)) @ A
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.0))
a1.plot(y, G / A[0], color=blu, lw=1.6, label="rettangolare")
a1.plot(y, np.sin(t), color=rame, lw=1.2, ls="--", label="ellittica")
a1.set_xlabel(r"$2y/b$", fontsize=9)
a1.set_title(r"$\Gamma/(2bV_\infty A_1)$", fontsize=9)
a1.legend(fontsize=8, frameon=False, loc="lower center")
a1.set_ylim(0, 1.25)
d = np.cumsum(n[1:] * (A[1:] / A[0])**2)
a2.plot(np.arange(1, len(d) + 1), d, "o-", color=blu, ms=4, lw=0.8)
a2.axhline(d[-1], color=rame, lw=0.8, ls="--")
a2.set_xlabel("numero di termini", fontsize=9)
a2.set_title(r"somme parziali di $\delta$", fontsize=9)
a2.set_ylim(0.040, 0.050)
for ax in (a1, a2):
    ax.tick_params(labelsize=8)
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/resistenza_indotta.png", dpi=220)

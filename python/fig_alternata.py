"""
fig_alternata.py — Capitolo 11, somme parziali della serie armonica
alternata attorno a log 2, con la fascia di errore a_(n+1).
Eseguire dalla cartella Libro/:  python3 python/fig_alternata.py
"""
import numpy as np
import matplotlib.pyplot as plt

blu, rame, grigio = "#1F4E79", "#B4662F", "#5A5A5A"
n = np.arange(1, 31)
s = np.cumsum((-1.0)**(n - 1) / n)
L = np.log(2)
fig, ax = plt.subplots(figsize=(6.0, 3.0))
nn = np.linspace(1, 30, 300)
ax.fill_between(nn, L - 1 / (nn + 1), L + 1 / (nn + 1),
                color="#C9D7E8", alpha=0.7, lw=0)
ax.plot(n, s, color=grigio, lw=0.6)
ax.plot(n[1::2], s[1::2], "o", color=blu, ms=4, label="$n$ pari")
ax.plot(n[0::2], s[0::2], "s", color=rame, ms=4, label="$n$ dispari")
ax.plot([0, 30.5], [L, L], color="k", lw=0.8, ls="--")
ax.text(31, L, r"$\log 2$", va="center", fontsize=9)
ax.set_xlabel("$n$", fontsize=9)
ax.set_ylabel("$s_n$", fontsize=9)
ax.set_xlim(0, 34)
ax.set_ylim(0.45, 1.05)
ax.legend(fontsize=8, frameon=False)
ax.tick_params(labelsize=8)
for sp_ in ("top", "right"):
    ax.spines[sp_].set_visible(False)
fig.tight_layout()
fig.savefig("figure/alternata.png", dpi=220)

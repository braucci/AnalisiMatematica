"""
fig_numero_e.py — Capitolo 3, le successioni (1+1/n)^n e (1+1/n)^(n+1).
Eseguire dalla cartella Libro/:  python3 python/fig_numero_e.py
"""
import math
import matplotlib.pyplot as plt

n = list(range(1, 41))
a = [(1 + 1/k) ** k for k in n]
b = [(1 + 1/k) ** (k + 1) for k in n]

fig, ax = plt.subplots(figsize=(7, 3.4))
ax.axhline(math.e, color="#5A5A5A", ls="--", lw=1)
ax.plot(n, a, "o", color="#1F4E79", ms=4, label=r"$a_n=(1+1/n)^n$")
ax.plot(n, b, "s", color="#B4662F", ms=3.6, label=r"$b_n=(1+1/n)^{n+1}$")
ax.text(42.6, math.e, r"$e$", va="center", fontsize=12, color="#5A5A5A",
        bbox=dict(fc="white", ec="none", pad=1))
ax.set_xlabel(r"$n$"); ax.set_ylim(1.9, 4.1); ax.set_xlim(0, 44)
ax.legend(frameon=False); ax.grid(alpha=0.25)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure/numero_e.png", dpi=220)
